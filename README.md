# Pirá: A Bilingual Portuguese-English Dataset for Question-Answering about the Ocean
Pirá [link] is a manually-constructed dataset of questions and answers about the ocean and the Brazilian coast. Questions were produced by undergraduate and graduate students based on two different corpora: 3891 abstracts of scientific papers on the Brazilian coast and two reports of the UN on the ocean ("World Ocean Assessment" I and II).

<img src="./methodology_overview.png">

Pirá is, to the best of our knowledge, the first QA dataset with supporting texts in Portuguese, and, perhaps more importantly, the first bilingual QA dataset that includes Portuguese as one of the languages. Pirá is also the first QA dataset in Portuguese with unanswerable questions so as to allow the study of answer triggering; finally, it is the first QA dataset that deals with scientific knowledge about the ocean, climate change, and marine biodiversity.

# Dataset description
The current version of the dataset, contains 2261 QA sets. Each QA set consists of up to four elements: four elements: a question in Portuguese and in English, and
an answer in Portuguese and in English. Around 90% of the QA sets also contain manual evaluations.

Each JSON file is in the following format:

....

Here's an example from the dataset:

....

# Web application
As part of the process of creating Pirá, we developed a web application for conducting the two phases of the experiment: QA creation and evaluation.

The code for the two parts of the application can be found here [link] [link].

# Citation
If you use or discuss this dataset in your work, please cite it as follows:
@inproceedings{x,
    title = "{Pirá: A Bilingual Portuguese-English Dataset for Question-Answering about the Ocean}",
    author = "x",
    booktitle = "x",
    year = "2021"
}


# License
Pirá dataset is licensed under CC BY 4.0.
