'MCQA-train.csv', 'MCQA-validation.csv', 'MCQA-test.csv' are the datasets for the multiple-choice question answering (MCQA) benchmark.

Script files:

UnifiedQA_finetuning.py: script with fine-tuning for UnifiedQA. It's a for loop that generates results for UnifiedQA base and large, with or without context (i.e., with or without the supporting text). 
- 'mcqa_results' contains the results of the fine-tuning for UnifiedQA

alternative_label.ipynb: script that used to create the column with the correct label name (e.g., 'A'), by using a F1-score between the with the correct answer and the alternatives.
