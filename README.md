# *Pirá*: A Bilingual Portuguese-English Dataset for Question-Answering about the Ocean
*Pirá* [link] is a manually-constructed dataset of questions and answers about the ocean and the Brazilian coast for reading comprehension. 

The dataset contains 2261 QA sets, as well as the texts they were created from. Each QA set contais up to four elements: a question in Portuguese and in English, and an answer in Portuguese and in English. Around 90% of the QA sets also contain manual evaluations.

Pirá is, to the best of our knowledge, the first QA dataset with supporting texts in Portuguese, and, perhaps more importantly, the first bilingual QA dataset that includes Portuguese as one of the languages. Pirá is also the first QA dataset in Portuguese with unanswerable questions so as to allow the study of answer triggering; finally, it is the first QA dataset that deals with scientific knowledge about the ocean, climate change, and marine biodiversity.

# Methodology
The dataset generation process is depicted above. Two different corpora of texts were collected: abstracts of scientific papers about the Brazilian coast, and small excerpts of two books about the ocean organized by the United Nations ("World Ocean Assessment" I and II). Next, a group of undergraduate and graduate volunteers elaborated questions based on these texts, both in English and Portuguese. Participants were instructed to produce questions that could be answered with the use of the texts and no other source of information. In a second step, the same volunteers assessed these QA sets in a number of ways. They were asked to: i) answer the question in both languages without having access to the original answer; ii) assess the whole original QA set (the questions and respective answers) according to a number of aspects; and iii) paraphrase the original question.

<img src="./methodology_overview.png" width=800>

# Dataset description
The dataset is available in three formats: JSON, CSV, and XLSX.

Each JSON file is in the following format:

....

Here's an example from the dataset:

....

# Web application
As part of the process of creating Pirá, we developed a web application for conducting the two phases of the experiment: QA creation and evaluation.

The code for the two parts of the application can be found here [link] [link].

# Citation
If you use or discuss this dataset in your work, please cite it as follows:
> @inproceedings{x,
    title = "{Pirá: A Bilingual Portuguese-English Dataset for Question-Answering about the Ocean}",
    author = "x",
    booktitle = "x",
    year = "2021"
}

If you use our dataset, please get in contact with us, so we can put reference it here.

# License
*Pirá* dataset is licensed under CC BY 4.0.
