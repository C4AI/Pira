import pandas as pd
import numpy as np
from datasets import Dataset, DatasetDict
import csv
from sklearn.metrics import f1_score, accuracy_score

## Parameters
languages = ['english', 'portuguese']
question_type = ['standard', 'human_paraphrase', 'automatic_paraphrase']
model_names = ['bert-base-uncased', 'bert-large-uncased',  'roberta-base', 'roberta-large',
               'neuralmind/bert-base-portuguese-cased']

# Create headline
with open('AT_results.csv', 'a') as fd:
    write = csv.writer(fd)
    write.writerow(['model_name', 'dataset_type', 'language', 'f1', 'acc'])

for language in languages:
    for model_name in model_names:

        if model_name in ['bert-base-uncased', 'roberta-base', 'neuralmind/bert-base-portuguese-cased']:
            batch_size = 16
        elif model_name in ['bert-large-uncased', 'roberta-large', 'neuralmind/bert-large-portuguese-cased']:
            batch_size = 8

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
                    train = train[['abstract', 'question_en_origin', 'question_en_paraphase', 'at_labels']]

                    # create list of permuting columns
                    question_columns = ['question_en_origin', 'question_en_paraphase']

                    new_dfs = []

                    for col in question_columns:
                        df_subset = train[['abstract', col, 'at_labels']].rename(
                            columns={col: 'question', 'at_labels': 'label'})
                        new_dfs.append(df_subset)

                    train = pd.concat(new_dfs)

                if language == 'portuguese':
                    # adding human paraphrases
                    train = train[['abstract', 'question_pt_origin', 'question_pt_paraphase', 'at_labels']]

                    # create list of permuting columns
                    question_columns = ['question_pt_origin', 'question_pt_paraphase']

                    new_dfs = []

                    for col in question_columns:
                        df_subset = train[['abstract', col, 'at_labels']].rename(
                            columns={col: 'question', 'at_labels': 'label'})
                        new_dfs.append(df_subset)

                    train = pd.concat(new_dfs)

            if questions == 'automatic_paraphrase':

                if language == 'english':
                    # adding automatic paraphrases
                    train = train[['abstract', 'question_en_origin', 'question_en_paraphase',
                                   'question_AUT_EN_1', 'question_AUT_EN_2', 'at_labels']]

                    question_columns = ['question_en_origin', 'question_en_paraphase',
                                        'question_AUT_EN_1', 'question_AUT_EN_2']

                    new_dfs = []

                    for col in question_columns:
                        df_subset = train[['abstract', col, 'at_labels']].rename(
                            columns={col: 'question', 'at_labels': 'label'})
                        new_dfs.append(df_subset)

                    train = pd.concat(new_dfs)

                if language == 'portuguese':
                    # adding automatic paraphrases
                    train = train[['abstract', 'question_pt_origin', 'question_pt_paraphase',
                                   'question_AUT_PT_1', 'question_AUT_PT_2', 'at_labels']]

                    question_columns = ['question_pt_origin', 'question_pt_paraphase',
                                        'question_AUT_PT_1', 'question_AUT_PT_2']

                    new_dfs = []

                    for col in question_columns:
                        df_subset = train[['abstract', col, 'at_labels']].rename(
                            columns={col: 'question', 'at_labels': 'label'})
                        new_dfs.append(df_subset)

                    train = pd.concat(new_dfs)

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

            # Change label data type
            train['label'] = train["label"].astype(int)
            validation['label'] = validation["label"].astype(int)
            test['label'] = test["label"].astype(int)

            ## Create context
            if model_name in ['bert-base-uncased', 'bert-large-uncased', 'neuralmind/bert-base-portuguese-cased',
                              'neuralmind/bert-large-portuguese-cased']:
                separator = '[SEP]'
            elif model_name in ['roberta-base', 'roberta-large']:
                separator = '</s></s>'

            train['text'] = train['abstract'] + separator + train['question']
            validation['text'] = validation['abstract'] + separator + validation['question']
            test['text'] = test['abstract'] + separator + test['question']

            # Balance dataset
            # determine the minimum number of rows for any given class
            #min_count = train['label'].value_counts().min()

            # group the dataframe by class and select a random subset of rows for each class based on the minimum count
            #train = train.groupby('label').apply(lambda x: x.sample(n=min_count))

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
                return tokenizer(examples["text"], truncation=True, padding=True, max_length=512)

            tokenized_text = my_dataset_dict.map(preprocess_function, batched=True)

            from transformers import DataCollatorWithPadding

            data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

            ### Train

            from transformers import AutoModelForSequenceClassification, TrainingArguments, Trainer

            model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

            training_args = TrainingArguments(
                    output_dir="./results",
                    learning_rate=2e-5,
                    per_device_train_batch_size=batch_size,
                    per_device_eval_batch_size=batch_size,
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

            with open('AT_results.csv', 'a') as fd:
                write = csv.writer(fd)
                write.writerow(result)