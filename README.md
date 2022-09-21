# *Pirá*: A Bilingual Portuguese-English Dataset for Question-Answering about the Ocean
*Pirá* is a crowdsourced question answering (QA) dataset on the ocean and the Brazilian coast designed for reading comprehension. You can download the full paper [here](https://dl.acm.org/doi/pdf/10.1145/3459637.3482012).

The dataset contains 2261 QA sets, as well as the texts associated with them. Each QA set contains at least four elements: a question in Portuguese and in English, and an answer in Portuguese and in English. Around 90% of the QA sets also contain human evaluations.

Pirá is, to the best of our knowledge, the first QA dataset with supporting texts in Portuguese, and, perhaps more importantly, the first bilingual QA dataset that includes Portuguese as one of its languages. Pirá is also the first QA dataset in Portuguese with unanswerable questions so as to allow the study of answer triggering. Finally, it is the first QA dataset that tackles scientific knowledge about the ocean, climate change, and marine biodiversity.

# Methodology
The dataset generation process is depicted below. Two different corpora of texts were collected: corpus 1 is composed of 3891 abstracts of scientific papers about the Brazilian coast from the Scopus database, and corpus 2 is composed of 189 small excerpts of two reports on the ocean organized by the United Nations ([World Ocean Assessment I](https://www.un.org/regularprocess/content/first-world-ocean-assessment) and [World Ocean Assessment II](https://www.un.org/regularprocess/woa2launch)). Undergraduate and graduate volunteers then created questions based on these texts, both in English and Portuguese. Participants were instructed to produce questions that could be answered with the use of the texts and no other source of information. In a second step, the same volunteers assessed these question sets in a number of ways. They were asked to: i) answer the question in both languages without having access to the original answer; ii) assess the whole original question-answer pair (QA sets) according to a number of aspects; and iii) paraphrase the original question.

<img src="./methodology_overview.png" width=800>

<br>
<br>

Here is an example of a question-answer pair set from Pirá:

```
{
    "id_qa": "B2142",
    "corpus": 2,
    "question_en_origin": "What are the proportion of men and women employed in the fishery sector worlwide?",
    "question_pt_origin": "Qual é a proporção de homens e mulheres empregados no setor pesqueiro em todo o mundo?",
    "question_en_paraphase": "Which share of the fishery sector workers of the world are women?",
    "question_pt_paraphase": "Qual parcela dos trabalhadores do setor da pesca no mundo são mulheres?",
    "answer_en_origin": "85 per cent men and 15 per cent women.",
    "answer_pt_origin": "85 por cento homens e 15 por cento mulheres.",
    "answer_en_validate": "It is estimated that more than fifteen per cent of the fishing sector workers are women.",
    "answer_pt_validate": "Estima-se que mais de quinze por cento dos trabalhadores do setor da pesca são mulheres.",
    "eid_article_scopus": "",
    "text_excerpts_un_reports": "Distribution of ocean benefits and disbenefits Developments in employment and income from fisheries and aquaculture The global harvest of marine capture fisheries has expanded rapidly since the early 1950s and is currently estimated to be about 80 million tons a year. That harvest is estimated to have a first (gross) value on the order of 113 billion dollars. Although it is difficult to produce accurate employment statistics, estimates using a fairly narrow definition of employment have put the figure of those employed in fisheries and aquaculture at 58.3 million people (4.4 per cent of the estimated total of economically active people), of which 84 per cent are in Asia and 10 per cent in Africa. Women are estimated to account for more than 15 per cent of people employed in the fishery sector. Other estimates, probably taking into account a wider definition of employment, suggest that capture fisheries provide direct and indirect employment for at least 120 million persons worldwide. Small-scale fisheries employ more than 90 per cent of the world’s capture fishermen and fish workers, about half of whom are women. When all dependants of those taking full- or part-time employment in the full value chain and support industries (boatbuilding, gear construction, etc.) of fisheries and aquaculture are included, one estimate concludes that between 660 and 820 million persons have some economic or livelihood dependence on fish capture and culture and the subsequent direct value chain. No sound information appears to be available on the levels of death and injury of those engaged in capture fishing or aquaculture, but capture fishing is commonly characterized as a dangerous occupation. Over time, a striking shift has occurred in the operation and location of capture fisheries. In the 1950s, capture fisheries were largely undertaken by developed fishing States. Since then, developing countries have increased their share. As a broad illustration, in the 1950s, the southern hemisphere accounted for no more than 8 per cent of landed values. By the last decade, the southern hemisphere’s share had risen to 20 per cent. In 2012, international trade represented 37 per cent of the total fish production in value, with a total export value of 129 billion dollars, of which 70 billion dollars (58 per cent) was exports by developing countries. Aquaculture is responsible for the bulk of the production of seaweeds. Worldwide, reports show that 24.9 million tons was produced in 2012, valued at about 6 billion dollars. In addition, about 1 million tons of wild seaweed were harvested. Few data were found on international trade in seaweeds, but their culture is concentrated in countries where consumption of seaweeds is high.",
    "question_generic": false,
    "answer_in_text": true,
    "answer_difficulty": 1,
    "question_meaningful": 5,
    "answer_equivalent": 5,
    "question_type": "None of the above"
  }
  ```

# Dataset description
*Pirá* is available in three formats: [JSON](https://github.com/C4AI/Pira/tree/main/JSON), [CSV](https://github.com/C4AI/Pira/tree/main/CSV), and [XLSX](https://github.com/C4AI/Pira/tree/main/XLSX).

It has three versions: *Pirá-F* (filtered), *Pirá-T* (triggering), and *Pirá-C* (complete).

- ***Pirá-F***. It includes only QA sets that volunteers indicated as not generic, that could be answered with only the information provided by the text, and moreover that volunteers agreed (4) or strongly agreed (5) that made sense. When volunteers reported in Phase 2 that their answer did not coincide with the original one (i.e., 1-2 in the Likert scale for “Your answer and the original answer are equivalent”), we excluded the new answer from the dataset. Finally, we also included the paraphrases. The dataset contains up to four possible combinations of QA sets: original question, original answer; original question, new answer; paraphrase, original answer; paraphrase, new answer.

- ***Pirá-T***. It is the answer-triggering version of the dataset. It includes all QA sets generated in Phases 1 and 2 (meaningful and meaningless, contextualized and non-contextualized, answered by the text only or not). As for *Parí-F*, we also excluded questions that were assessed with one or two points for the statement “Your answer and the original answer are equivalent”. In addition, the answers (original e new) for questions that volunteers regarded meaningless (1-2 in the Likert scale for “The question makes sense”) were filled with “ ” (blank value). In datasets that every question possess an answer, models can always guess an answer (and sometimes be right just by luck). Instead, by allowing some questions not to have an answer, models are required to learn when they are able to answer a given question, a task known as “answer triggering” (which is getting more important in QA datasets).

- ***Pirá-C***. For the sake of completeness, we also make available *Pirá-C*, with all the questions and answers produced in the generation and assessment phases.

<center>

| Version  |  #QA sets  |
| ------------------- | ------------------- |
|  *Pirá-F* |  1347 |
|  *Pirá-T* |  2070 |
|  *Pirá-C* |  2272 |

</center>

# Baselines
Five benchmarks have been created for Pirá 2.0: machine reading comprehension, information retrieval, open question answering, answer triggering, and multiple-choice question answering. Codes for them are available at this page.


Baselines for these benchmarks are reported above:

## Machine Reading Comprehension
Definição da tarefa


# Web application
As part of the process of creating Pirá, we developed a web application for conducting the two phases of the experiment: QA creation and evaluation.

The code for the two parts of the application can be found in [data-set-builder](https://github.com/C4AI/data-set-builder) and [data-set-validator](https://github.com/C4AI/data-set-validator).

# Citation
If you use or discuss this dataset in your work, please cite it as follows. 

For the original paper:

```
@inproceedings{10.1145/3459637.3482012,
author = {Paschoal, Andr\'{e} F. A. and Pirozelli, Paulo and Freire, Valdinei and Delgado, Karina V. and Peres, Sarajane M. and Jos\'{e}, Marcos M. and Nakasato, Fl\'{a}vio and Oliveira, Andr\'{e} S. and Brand\~{a}o, Anarosa A. F. and Costa, Anna H. R. and Cozman, Fabio G.},
title = {Pir\'{a}: A Bilingual Portuguese-English Dataset for Question-Answering about the Ocean},
year = {2021},
isbn = {9781450384469},
publisher = {Association for Computing Machinery},
address = {New York, NY, USA},
url = {https://doi.org/10.1145/3459637.3482012},
doi = {10.1145/3459637.3482012},
abstract = {Current research in natural language processing is highly dependent on carefully produced
corpora. Most existing resources focus on English; some resources focus on languages
such as Chinese and French; few resources deal with more than one language. This paper
presents the Pir\'{a} dataset, a large set of questions and answers about the ocean and
the Brazilian coast both in Portuguese and English. Pir\'{a} is, to the best of our knowledge,
the first QA dataset with supporting texts in Portuguese, and, perhaps more importantly,
the first bilingual QA dataset that includes this language. The Pir\'{a} dataset consists
of 2261 properly curated question/answer (QA) sets in both languages. The QA sets
were manually created based on two corpora: abstracts related to the Brazilian coast
and excerpts of United Nation reports about the ocean. The QA sets were validated
in a peer-review process with the dataset contributors. We discuss some of the advantages
as well as limitations of Pir\'{a}, as this new resource can support a set of tasks in
NLP such as question-answering, information retrieval, and machine translation.},
booktitle = {Proceedings of the 30th ACM International Conference on Information & Knowledge Management},
pages = {4544–4553},
numpages = {10},
keywords = {Portuguese-English dataset, question-answering dataset, bilingual dataset, ocean dataset},
location = {Virtual Event, Queensland, Australia},
series = {CIKM '21}
}
```

For the Pirá 2.0 dataset or the baselines:



# Applications
Cação, F. N., José, M. M., Oliveira, A. S., Spindola, S., Costa, A. H. R., & Cozman, F. G. (2021). [DEEPAGÉ: Answering Questions in Portuguese about the Brazilian Environment](https://arxiv.org/pdf/2110.10015.pdf).

Rodrigues, L. A., & Vieira, M. H. D. S. (2021). [Autosumm: Architecture for a Multi-Document Abstractive Summarization System](https://pcs.usp.br/pcspf/wp-content/uploads/sites/8/2021/12/Monografia_PCS3560_SEM_2021_Grupo_S20.pdf).

Cação, F. N., Costa, A. H. R., Unterstell, N., Yonaha, L., Stec, T., & Ishisaki, F. (2022). [Tracking environmental policy changes in the Brazilian Federal Official Gazette. In International Conference on Computational Processing of the Portuguese Language](10.1007/978-3-030-98305-5_24). Springer, Cham, p. 256-66.

Pellicer, L. F. A. O., Pirozelli, P., Costa, A. H. R., & Inoue, A. (2022). [PTT5-Paraphraser: Diversity and Meaning Fidelity in Automatic Portuguese Paraphrasing. In International Conference on Computational Processing of the Portuguese Language](10.1007/978-3-030-98305-5_28). Springer, Cham, p. 299-309.

In case you cite our work, please contact us: we will be very happy of referencing it here. E-mail: paulo.pirozelli.silva@usp.br.

# License
*Pirá* dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Scopus adopts a license–based approach which automatically enables researchers at subscribing institutions to text mine for non-commercial research purposes and to gain access to full text content in XML for this purpose. More information can be found [here](https://www.elsevier.com/about/policies/text-and-data-mining).

The United Nations' Reports on the ocean are freely accessible from the links above.

This work was carried out at the [Center for Artificial Intelligence](http://c4ai.inova.usp.br/) at the University of São Paulo (C4AI-USP), with support by the São Paulo Research Foundation (FAPESP grant #2019/07665-4) and by the IBM Corporation.

<img src="./C4AI_logo.jpeg" width=300>
