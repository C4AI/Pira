# Naive bayes
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.metrics import accuracy_score, f1_score
import pandas as pd
import csv

question_type = ['standard', 'human_paraphrase', 'automatic_paraphrase']
languages = ['english', 'portuguese']

# Create headline
with open('naive_bayes.csv', 'a') as fd:
    write = csv.writer(fd)
    write.writerow(['model_name', 'dataset_version', 'language', 'f1_NB', 'acc_NB', 'f1_CA', 'acc_CA'])

for language in languages:

    for questions in question_type:

        train, test = pd.read_csv('train.csv'), pd.read_csv('test.csv')

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

                train_1.columns = ['abstract_translated_pt', 'question', 'label']
                train_2.columns = ['abstract_translated_pt', 'question', 'label']
                train_3.columns = ['abstract_translated_pt', 'question', 'label']
                train_4.columns = ['abstract_translated_pt', 'question', 'label']

                frames = [train_1, train_2, train_3, train_4]

                train = pd.concat(frames)

        if language == 'english':
            test = test[['abstract', 'question_en_origin', 'at_labels']]
            test.rename(columns={'question_en_origin': 'question', 'at_labels': 'label'}, inplace=True)

        if language == 'portuguese':
            test = test[['abstract_translated_pt', 'question_pt_origin', 'at_labels']]
            test.rename(columns={'abstract_translated_pt': 'abstract',
                                 'question_pt_origin': 'question', 'at_labels': 'label'}, inplace=True)

        train = train.dropna()
        test = test.dropna()

        ## Train model
        model = make_pipeline(TfidfVectorizer(), MultinomialNB())
        model.fit(train['question'].values, train['label'].values)

        # Validate the model
        preds = model.predict(list(test['question']))

        acc = accuracy_score(test['label'].values, preds) * 100
        f1_weighted = f1_score(test['label'].values, preds, average='weighted') * 100

        # Class assignment
        max_assignment = [1 for i in range(len(test))]
        f1_max_class = f1_score(test['label'].values, max_assignment, average='weighted') * 100
        acc_CA = accuracy_score(test['label'].values, max_assignment) * 100

        result = [questions, language, f1_weighted, acc, f1_max_class, acc_CA]

        # Save results
        with open('naive_bayes.csv', 'a') as fd:
            write = csv.writer(fd)
            write.writerow(result)
