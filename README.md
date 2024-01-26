## ML Project: Searching for Proteins Capable of Binding DNA or RNA

### Overview

* The goal of this project is to develop a machine learning (ML) model that can identify proteins capable of binding DNA or RNA. This project is significant because DNA and RNA binding proteins play a crucial role in a variety of biological processes, including gene regulation, transcription, and translation. By developing an ML model that can identify these proteins, we can gain a better understanding of these processes and develop new drugs and therapies
* Given the distinct biochemical and physical characteristics of DNA and RNA, we have made a strategic decision to treat the task of predicting protein binding as two independent binary classification problems: one for DNA binding and another for RNA binding. This decision is grounded in the understanding that DNA and RNA interactions with proteins involve unique molecular features and binding motifs


### Data
* It includes carefully curated experimental data of proteins from [Uniprot](https://www.uniprot.org/) database having experimental evidence and 3D structure in [PDB](https://www.rcsb.org/) database
* It also includes experimentally unconfirmed data, but having the appropriate molecular annotation [InterPro](https://www.ebi.ac.uk/interpro/) database

As a component of the experiment, we aim to assess the generalization capabilities of models trained on non-experimentally confirmed data to predict and perform effectively on experimental datasets

1. DNA Binding Dataset (DBP)
* Source: [Benchmark data from papers](data/DBP_papers_data/benchmark_data.csv)
* Description: Thr Benchmark data collected from scientific papers
* Source: [NAKB PDB database](data/nakb/)
* Description: Thr experimental data collected from NAKB PDB database



2.RNA Binding Dataset 
* Coming soon ...


### Notebooks
* [Parse supplementary data and processing protein sequences](notebooks/parse_papers_data.ipynb)


### Methods
We depart from traditional training approaches by leveraging the pre-trained [Ankh language model](https://arxiv.org/pdf/2301.06568.pdf) to extract physico-chemical features from the primary structure of proteins. Subsequently, these features are employed to train a classification model designed for predicting binding events. The chosen classification model is a gradient boosting algorithm, 
consisting of an ensemble of decision trees, selected for its effectiveness in capturing intricate patterns within the data.