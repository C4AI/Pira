import pandas as pd
import numpy as np
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, \
    DataCollatorForSeq2Seq, Seq2SeqTrainingArguments, Seq2SeqTrainer
from datasets import Dataset, DatasetDict, load_metric
import string
from collections import Counter
import csv

metric = load_metric("sacrebleu")
batch_size = 16
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Create headline
with open('mcqa_results.csv', 'a') as fd:
    write = csv.writer(fd)
    write.writerow(['model_name', 'context', 'acc'])


model_names = ["allenai/unifiedqa-t5-base", "allenai/unifiedqa-t5-large"]
input_types = ['no_context', 'with_context']

for model_name in model_names:

    if model_name == "allenai/unifiedqa-t5-base":
        batch_size = 16
    elif model_name == "allenai/unifiedqa-t5-large":
        batch_size = 4

    for input_type in input_types:

        # Load datasets
        train, validation, test = pd.read_csv('MCQA-train.csv'), \
            pd.read_csv('MCQA-validation.csv'), pd.read_csv('MCQA-test.csv')


        # create a new column by concatenating strings with values of ColumnA and ColumnB
        for dataset in [train, validation, test]:
            if input_type == 'no_context':
                dataset['full_question'] = dataset['question'] + r"\\n" + ' (A) ' + dataset['A'] + ' (B) ' + dataset[
                    'B'] + ' (C) ' + dataset['C'] + ' (D) ' + dataset['D'] + ' (E) ' + dataset['E']
            elif input_type == 'with_context':
                dataset['full_question'] = dataset['text'] + r"\\n" + dataset['question'] + r"\\n" + ' (A) ' + dataset['A'] + ' (B) ' + dataset['B'] + ' (C) ' + dataset['C'] + ' (D) ' + dataset['D'] + ' (E) ' + dataset['E']

        # Convert dataframe into dict
        train_dataset = Dataset.from_pandas(train)
        validation_dataset = Dataset.from_pandas(validation)
        test_dataset = Dataset.from_pandas(test)

        my_dataset_dict = DatasetDict({"train": train_dataset,
                                       'validation': validation_dataset, "test": test_dataset})


        # Tokenizer
        tokenizer = AutoTokenizer.from_pretrained(model_name)

        prefix = ''
        max_input_length = 512
        max_target_length = 128

        def preprocess_function(examples):
            inputs = examples["full_question"]
            targets = examples["correct"]
            model_inputs = tokenizer(inputs, max_length=max_input_length, truncation=True)

            # Setup the tokenizer for targets
            with tokenizer.as_target_tokenizer():
                labels = tokenizer(targets, max_length=max_target_length, truncation=True)

            model_inputs["labels"] = labels["input_ids"]
            return model_inputs

        tokenized_datasets = my_dataset_dict.map(preprocess_function, batched=True)

        # Model
        model = AutoModelForSeq2SeqLM.from_pretrained(model_name).to(device)

        args = Seq2SeqTrainingArguments(
            f"{model_name}-finetuned",
            evaluation_strategy = "epoch",
            learning_rate=2e-5,
            per_device_train_batch_size=batch_size,
            per_device_eval_batch_size=batch_size,
            weight_decay=0.01,
            save_total_limit=3,
            num_train_epochs=40,
            predict_with_generate=True,
            fp16=False,
            push_to_hub=False,
        )

        data_collator = DataCollatorForSeq2Seq(tokenizer, model=model)

        def postprocess_text(preds, labels):
            preds = [pred.strip() for pred in preds]
            labels = [[label.strip()] for label in labels]

            return preds, labels

        def compute_metrics(eval_preds):
            preds, labels = eval_preds
            if isinstance(preds, tuple):
                preds = preds[0]
            decoded_preds = tokenizer.batch_decode(preds, skip_special_tokens=True)

            # Replace -100 in the labels as we can't decode them.
            labels = np.where(labels != -100, labels, tokenizer.pad_token_id)
            decoded_labels = tokenizer.batch_decode(labels, skip_special_tokens=True)

            # Some simple post-processing
            decoded_preds, decoded_labels = postprocess_text(decoded_preds, decoded_labels)

            result = metric.compute(predictions=decoded_preds, references=decoded_labels)
            result = {"bleu": result["score"]}

            prediction_lens = [np.count_nonzero(pred != tokenizer.pad_token_id) for pred in preds]
            result["gen_len"] = np.mean(prediction_lens)
            result = {k: round(v, 4) for k, v in result.items()}
            return result

        trainer = Seq2SeqTrainer(
            model,
            args,
            train_dataset=tokenized_datasets["train"],
            eval_dataset=tokenized_datasets["validation"],
            data_collator=data_collator,
            tokenizer=tokenizer,
            compute_metrics=compute_metrics
        )

        trainer.train()

        ### Inference
        # Return model to cpu
        model = model.to('cpu')

        def run_model(input_string, **generator_args):
            input_ids = tokenizer.encode(input_string, return_tensors="pt")
            res = model.generate(input_ids, **generator_args)
            return tokenizer.batch_decode(res, skip_special_tokens=True)

        predictions = []

        for sample in test['full_question']:
            pred = run_model(sample)[0]
            predictions.append(pred)

        test['predictions'] = predictions

        # Calculate accuracy
        # function to calculate overlap
        def normalize_answer(s):
            """Lower text and remove punctuation and extra whitespace."""

            def white_space_fix(text):
                return ' '.join(text.split())

            def remove_punc(text):
                exclude = set(string.punctuation)
                return ''.join(ch for ch in text if ch not in exclude)

            def lower(text):
                return text.lower()

            return white_space_fix(remove_punc(lower(s)))

        def f1_score(prediction, ground_truth):
            prediction_tokens = normalize_answer(prediction).split()
            ground_truth_tokens = normalize_answer(ground_truth).split()
            common = Counter(prediction_tokens) & Counter(ground_truth_tokens)
            num_same = sum(common.values())
            if num_same == 0:
                return 0
            precision = 1.0 * num_same / len(prediction_tokens)
            recall = 1.0 * num_same / len(ground_truth_tokens)
            f1 = (2 * precision * recall) / (precision + recall) * 100
            return f1

        # apply comparison function between values in Column3 and all other columns
        test['Comparison_A'] = test.apply(lambda x: f1_score(x['A'], x['predictions']), axis=1)
        test['Comparison_B'] = test.apply(lambda x: f1_score(x['B'], x['predictions']), axis=1)
        test['Comparison_C'] = test.apply(lambda x: f1_score(x['C'], x['predictions']), axis=1)
        test['Comparison_D'] = test.apply(lambda x: f1_score(x['D'], x['predictions']), axis=1)
        test['Comparison_E'] = test.apply(lambda x: f1_score(x['E'], x['predictions']), axis=1)

        # create new column with name of column with highest value
        df_subset = test.loc[:, ['Comparison_A', 'Comparison_B', 'Comparison_C', 'Comparison_D', 'Comparison_E']]

        test['answer_predicted'] = df_subset.idxmax(axis=1).str[-1]

        count = (test['alternative'] == test['answer_predicted']).sum()
        acc = count/len(test) * 100

        # Save results in csv
        with open('mcqa_results.csv', 'a') as fd:
            write = csv.writer(fd)
            write.writerow([model_name, input_type, acc])
