# *Pirá*: A Bilingual Portuguese-English Dataset for Question-Answering about the Ocean
*Pirá* [link] is a manually-constructed dataset of questions and answers about the ocean and the Brazilian coast designed for reading comprehension. 

This dataset contains 2261 QA sets, as well as the texts associated with them. Each QA set contais up to four elements: a question in Portuguese and in English, and an answer in Portuguese and in English. Around 90% of the QA sets also contain manual evaluations.

Pirá is, to the best of our knowledge, the first QA dataset with supporting texts in Portuguese, and, perhaps more importantly, the first bilingual QA dataset that includes Portuguese as one of the languages. Pirá is also the first QA dataset in Portuguese with unanswerable questions so as to allow the study of answer triggering; finally, it is the first QA dataset that deals with scientific knowledge about the ocean, climate change, and marine biodiversity.

# Methodology
The dataset generation process is depicted above. Two different corpora of texts were collected: abstracts of scientific papers about the Brazilian coast, and small excerpts of two books about the ocean organized by the United Nations ([World Ocean Assessment I](https://www.un.org/regularprocess/content/first-world-ocean-assessment) and [World Ocean Assessment II](https://www.un.org/regularprocess/woa2launch)). Undergraduate and graduate volunteers then created questions based on these texts, both in English and Portuguese. Participants were instructed to produce questions that could be answered with the use of the texts and no other source of information. In a second step, the same volunteers assessed these QA sets in a number of ways. They were asked to: i) answer the question in both languages without having access to the original answer; ii) assess the whole original QA set (the questions and respective answers) according to a number of aspects; and iii) paraphrase the original question.

<img src="./methodology_overview.png" width=800>

Here is example of QA set from Pirá:

```
EXEMPLO - Pegar um exemplo do corpus 2
```

# Dataset description
*Pirá* is available in three formats: JSON, CSV, and XLSX.

It has three versions: *Pirá-F* (filtered), *Pirá-T* (triggering), and *Pirá-C* (complete).

*Pirá-F* includes only QA sets that volunteers indicated as not generic, that could be answered with only the information provided by the text, and moreover that volunteers agreed (4) or strongly agreed (5) that made sense. When volunteers reported in Phase 2 that their answer did not coincide with the original one (i.e., 1-2 in the Likert scale for “Your answer and the original answer are equivalent”), we excluded the new answer from the dataset. Finally, we also included the paraphrases. The dataset contains up to four possible combinations of QA sets: original question, original answer; original question, new answer; paraphrase, original answer; paraphrase, new answer.

*Pirá-T* is the answer-triggering version of the dataset. It includes all QA sets generated in Phases 1 and 2 (meaningful and meaningless, contextualized and non-contextualized, answered by the text only or not). As for *Parí-F*, we also excluded questions that were assessed with one or two points for the statement “Your answer and the original answer are equivalent”. In addition, the answers (original e new) for questions that volunteers regarded meaningless (1-2 in the Likert scale for “The question makes sense”) were filled with “ ” (blank value). In datasets that every question possess an answer, models can always guess an answer (and sometimes be right just by luck). Instead, by allowing some questions not to have an answer, models are required to learn when they are able to answer a given question, a task known as “answer triggering” (which is getting more important in QA datasets).

For the sake of completeness, we also make available *Pirá-C*, with all the questions and answers produced in the generation and assessment phases.

| Version  |  #QA sets  |
| ------------------- | ------------------- |
|  *Pirá-F* |  x |
|  *Pirá-T* |  x |
|  *Pirá-C* |  x |

# Web application
As part of the process of creating Pirá, we developed a web application for conducting the two phases of the experiment: QA creation and evaluation.

The code for the two parts of the application can be found in [data-set-builder](https://github.com/C4AI/data-set-builder) and [data-set-validator](https://github.com/C4AI/data-set-validator).

# Citation
If you use or discuss this dataset in your work, please cite it as follows:

```
@inproceedings{x,
    title = "{Pirá: A Bilingual Portuguese-English Dataset for Question-Answering about the Ocean}",
    author = "x",
    booktitle = "x",
    year = "2021"
}
```

If you use our dataset, please get in contact with us, so we can reference it here.

# License
*Pirá* dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).
