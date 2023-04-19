import pandas as pd
import numpy as np
from datasets import Dataset, DatasetDict
import csv
from sklearn.metrics import f1_score, accuracy_score

## Parameters
languages = ['english', 'portuguese']
question_type = ['standard', 'human_paraphrase', 'automatic_paraphrase']
model_names = ['bert-base-uncased', 'bert-large-uncased', 'roberta-base', 'roberta-large']

# Create headline
with open('transformers.csv', 'a') as fd:
    write = csv.writer(fd)
    write.writerow(['model_name', 'dataset_type', 'language', 'f1', 'acc'])

for language in languages:
    for model_name in model_names:
        for questions in question_type:

            train, validation, test = pd.read_csv('train.csv'), pd.read_csv('validation.csv'), pd.read_csv('test.csv')

            if questions == 'standard':

                if language == 'english':
                    train = train[['abstract', 'question_en_origin', 'at_labels']]

                    train.rename(columns={'question_en_origin': 'question', 'at_labels': 'label'}, inplace=True)

                if language == 'portuguese':
                    train = train[['abstract_translated_pt', 'question_pt_origin', 'at_labels']]

                    train.rename(columns={'abstract_translated_pt': 'abstract', 'question_pt_origin': 'question',
                                      'at_labels': 'label'}, inplace=True)

            if questions == 'human_paraphrase':

                if language == 'english':
                    # adding human paraphrases
                    train_1 = train[['abstract', 'question_en_origin', 'at_labels']]
                    train_2 = train[['abstract', 'question_en_paraphase', 'at_labels']]

                    train_1.columns = ['abstract', 'question', 'label']
                    train_2.columns = ['abstract', 'question', 'label']

                    frames = [train_1, train_2]

                    train = pd.concat(frames)

                if language == 'portuguese':
                    # adding human paraphrases
                    train_1 = train[['abstract_translated_pt', 'question_pt_origin', 'at_labels']]
                    train_2 = train[['abstract_translated_pt', 'question_pt_paraphase', 'at_labels']]

                    train_1.columns = ['abstract', 'question', 'label']
                    train_2.columns = ['abstract', 'question', 'label']

                    frames = [train_1, train_2]

                    train = pd.concat(frames)

            if questions == 'automatic_paraphrase':

                if language == 'english':
                    # adding automatic paraphrases
                    train_1 = train[['abstract', 'question_en_origin', 'at_labels']]
                    train_2 = train[['abstract', 'question_en_paraphase', 'at_labels']]
                    train_3 = train[['abstract', 'question_AUT_EN_1', 'at_labels']]
                    train_4 = train[['abstract', 'question_AUT_EN_2', 'at_labels']]

                    train_1.columns = ['abstract', 'question', 'label']
                    train_2.columns = ['abstract', 'question', 'label']
                    train_3.columns = ['abstract', 'question', 'label']
                    train_4.columns = ['abstract', 'question', 'label']

                    frames = [train_1, train_2, train_3, train_4]

                    train = pd.concat(frames)

                if language == 'portuguese':
                    # adding automatic paraphrases
                    train_1 = train[['abstract_translated_pt', 'question_pt_origin', 'at_labels']]
                    train_2 = train[['abstract_translated_pt', 'question_pt_paraphase', 'at_labels']]
                    train_3 = train[['abstract_translated_pt', 'question_AUT_PT_1', 'at_labels']]
                    train_4 = train[['abstract_translated_pt', 'question_AUT_PT_2', 'at_labels']]

                    train_1.columns = ['abstract', 'question', 'label']
                    train_2.columns = ['abstract', 'question', 'label']
                    train_3.columns = ['abstract', 'question', 'label']
                    train_4.columns = ['abstract', 'question', 'label']

                    frames = [train_1, train_2, train_3, train_4]

                    train = pd.concat(frames)

            if language == 'english':
                validation = validation[['abstract', 'question_en_origin', 'at_labels']]
                test = test[['abstract', 'question_en_origin', 'at_labels']]
                validation.rename(columns={'question_en_origin': 'question', 'at_labels': 'label'}, inplace=True)
                test.rename(columns={'question_en_origin': 'question', 'at_labels': 'label'}, inplace=True)

            if language == 'portuguese':
                validation = validation[['abstract_translated_pt', 'question_pt_origin', 'at_labels']]
                test = test[['abstract_translated_pt', 'question_pt_origin', 'at_labels']]
                validation.rename(columns={'abstract_translated_pt': 'abstract',
                                           'question_pt_origin': 'question', 'at_labels': 'label'}, inplace=True)
                test.rename(columns={'abstract_translated_pt': 'abstract',
                                     'question_pt_origin': 'question', 'at_labels': 'label'}, inplace=True)


            # Remove question without evaluation
            train = train.dropna()
            validation = validation.dropna()
            test = test.dropna()

            # Change label data type
            train['label'] = train["label"].astype(int)
            validation['label'] = validation["label"].astype(int)
            test['label'] = test["label"].astype(int)

            ## Create context
            if model_name in ['bert-base-uncased', 'bert-large-uncased']:
                separator = '[SEP]'
            elif model_name in ['roberta-base', 'roberta-large']:
                separator = '</s></s>'

            train['text'] = train['abstract'] + separator + train['question']
            validation['text'] = validation['abstract'] + separator + validation['question']
            test['text'] = test['abstract'] + separator + test['question']

            # Convert dataframe into dict
            train_dataset = Dataset.from_pandas(train)
            validation_dataset = Dataset.from_pandas(validation)
            test_dataset = Dataset.from_pandas(test)

            my_dataset_dict = DatasetDict({"train": train_dataset,
                                                    'validation': validation_dataset, "test": test_dataset})

            my_dataset_dict = my_dataset_dict.remove_columns(["__index_level_0__"])

            ## Classification
            ### Tokenizer
            from transformers import AutoTokenizer

            tokenizer = AutoTokenizer.from_pretrained(model_name)

            def preprocess_function(examples):
                return tokenizer(examples["text"], truncation=True, padding=True)

            tokenized_text = my_dataset_dict.map(preprocess_function, batched=True)

            from transformers import DataCollatorWithPadding

            data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

            ### Train

            from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

            model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

            training_args = TrainingArguments(
                    output_dir="./results",
                    learning_rate=2e-5,
                    per_device_train_batch_size=8,
                    per_device_eval_batch_size=8,
                    num_train_epochs=8,
                    weight_decay=0.01,
                    save_total_limit=1,
                    overwrite_output_dir=True,
                    load_best_model_at_end=True,
                    save_strategy="no",
                    seed=42
                )

            trainer = Trainer(
                    model=model,
                    args=training_args,
                    train_dataset=tokenized_text["train"],
                    eval_dataset=tokenized_text["validation"],
                    tokenizer=tokenizer,
                    data_collator=data_collator,
                )

            trainer.train()

            ## Prediction

            results = trainer.predict(tokenized_text['test']).predictions

            test['predictions'] = np.argmax(results, axis=-1)

            ## Metrics
            f1 = f1_score(test['label'], test['predictions'], average = 'weighted')
            acc = accuracy_score(test['label'], test['predictions'])

            print('F1-score:', f1)
            print('Accuracy:', acc)

            result = [model_name, questions, language, f1, acc]

            with open('transformers.csv', 'a') as fd:
                write = csv.writer(fd)
                write.writerow(result)
