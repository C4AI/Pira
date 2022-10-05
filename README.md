# *Pirá*: A Bilingual Portuguese-English Dataset for Question-Answering about the Ocean, the Brazilian coast, and climate change
*Pirá* is a crowdsourced reading comprehension dataset on the ocean, the Brazilian coast, and climate change. QA sets are presented in both Portuguese and English; the dataset also contains human paraphrases and assessments. 

The original paper was published at CIKM'21 and can be found [here](https://dl.acm.org/doi/pdf/10.1145/3459637.3482012). As a subsequent project, we have produced a curated version of the dataset, which we refer to as Pirá 2.0. In this step, we have also defined a number of benchmarks and reported the corresponding baselines. Pirá 2.0's preprint is available [here](https://assets.researchsquare.com/files/rs-2046889/v1_covered.pdf?c=1663082327).

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
Pirá contains 2258 QA sets, as well as supporting texts associated with them. Each QA set contains at least four elements: a question in Portuguese and in English, and an answer in Portuguese and in English. Around 90% of the QA sets also contain human evaluations. 

For Pirá 2.0, the original dataset has been completely revised for grammar issues, misplaced entries, repeated questions, plus other minor flaws. In addition to that, we extended the dataset in several directions. First, the new dataset includes automatic translations of the supporting texts into Portuguese, allowing us to run the benchmarks in this language as well. Second, we provide classification labels indicating whether a question can be answered or not, which are essential to the answer triggering benchmark. Third, Pirá 2.0 offers a multiple-choice QA extension, where each question has five candidate answers, of which only one is correct. Finally, Pirá 2.0 brings automatically-generated paraphrases for questions and answers in both Portuguese and English, a valuable data augmentation addition for training larger models.

We organize the dataset in two different files:

### Standard dataset
- Contains the supporting texts, QA sets, manual paraphrases, human assessments, and automatic paraphrases.

- Benchmarks supported: machine reading comprehension, information retrieval, open question answering, answer triggering, and multiple-choice question answering.

### Multiple-choice QA
- Contains the supporting texts, candidate answers, and the label for the correct answer.

- Benchmark supported: multiple-choice question answering.

### Pirá 1.0
The original dataset is available here.

# Baselines
Five benchmarks have been created for Pirá 2.0: machine reading comprehension, information retrieval, open question answering, answer triggering, and multiple-choice question answering. Codes for the experiments reported in Pirá 2.0 are available at this page.

A brief description of each bechmark is provided above, as well as the results for the best baselines in Portuguese and English:

## Machine Reading Comprehension
In Machine Reading Comprehension (MRC), the goal is to predict a span in the supporting text that answers a given question.

Results in English:
| Model type | Model | Fine-tuned | MSL | F1 | EM |
|---|---|---|---|---|---|
| Extractive | BERT Base | SQuAD 1 | 512 | 41.54 | 11.01 |
| Extractive | BERT Large | SQuAD 2 | 512 | 46.96 | 12.34 |
| Extractive | RoBERTa Base | SQuAD 2 | 512 | 47.65 | 13.66 |
| **Extractive** | **RoBERTa Large** | **SQuAD 2** | **512** | **48.22** | **12.78**|
| Extractive | ELECTRA Large | SQuAD 2 | 512 | 46.20 | 11.89 |
||
| Generative | T5 Base | SQuAD 2/Pirá 2 | 512 | 49.12 | 9.78 |
| Generative | T5 Base | SQuAD 2/Pirá 2 | 1024 | 50.50 | 11.56 |
| **Generative** | **T5 Base** | **SQuAD 2/Pirá 2** | **1536** | **51.27** | **13.33** |
| Generative | T5 Large | SQuAD 2/Pirá 2 | 512 | 41.22 | 10.67 |

Results in Portuguese:
| Model type | Model | Fine-tuned | MSL | F1 | EM |
|---|---|---|---|---|---|
| Extractive | BERTimbau | Squad 1.1 | 512 | 37.53 | 4.44 |
| Generative | PTT5 Base | Pirá 2 | 1536 | 27.90 | 4.44 |
| Generative | mT5 Base | SQuAD 2/Pirá 2 | 512 | 14.23 | 0.00 |

## Information Retrieval
Information Retrieval is the task of traversing a corpus C and delivering the _k_ most relevant documents for a query _q_.

## Open Question Answering
Open Question Answering combines the two previous tasks in one: given a question, one has to find the corresponding texts and generate an answer based on them.

## Answer Triggering
Answer Triggering is the problem of finding which questions should be answered and which ones should not; the “answerability” label are created from the manual assessments for question meaningfulness found on Pirá. 

##  Multiple-Choice Question Answering
In Multiple Choice Question Answer, each question has five alternative answers, and the goals is to find the correct one.


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

# Applications
Rodrigues, L. A., & Vieira, M. H. D. S. (2021). [Autosumm: Architecture for a Multi-Document Abstractive Summarization System](https://pcs.usp.br/pcspf/wp-content/uploads/sites/8/2021/12/Monografia_PCS3560_SEM_2021_Grupo_S20.pdf).

Pellicer, L. F. A. O., Pirozelli, P., Costa, A. H. R., & Inoue, A. (2022). [PTT5-Paraphraser: Diversity and Meaning Fidelity in Automatic Portuguese Paraphrasing. In International Conference on Computational Processing of the Portuguese Language](10.1007/978-3-030-98305-5_28). Springer, Cham, p. 299-309.

Pirozelli, P., Brandão, A. A. F., Peres, S. M., Cozman, F. G. (2022). To Answer or not to Answer? Filtering Questions for QA Systems. 11th Brazilian Conference on Intelligent Systems (BRACIS).

In case you cite our work, please contact us: we will be very happy of referencing it here. E-mail: paulo.pirozelli.silva@usp.br.

# License
*Pirá* dataset is licensed under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

Scopus adopts a license–based approach which automatically enables researchers at subscribing institutions to text mine for non-commercial research purposes and to gain access to full text content in XML for this purpose. More information can be found [here](https://www.elsevier.com/about/policies/text-and-data-mining).

The United Nations' Reports on the ocean are freely accessible through the links above.

This work was carried out at the [Center for Artificial Intelligence](http://c4ai.inova.usp.br/) at the University of São Paulo (C4AI-USP), with support by the São Paulo Research Foundation (FAPESP grant #2019/07665-4) and by the IBM Corporation. It is part of the Knowledge-Enhanced Machine Learning for Reasoning about Ocean Data (KEML), a project that aims to developed a [BLue Amazon Brain](https://arxiv.org/pdf/2209.07928.pdf). 

<img src="./C4AI_logo.jpeg" width=300>
