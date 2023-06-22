<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Train NER and SpanCat pipelines on LitBank entity and event annotations.

This project was used in the DH2023 Workshop in Graz to demonstrate how to
use spaCy to quickly put together useful pipelines.

The [LitBank dataset](https://github.com/dbamman/litbank/) is a collection of a 100 works of fiction
publicly available from Project Gutenberg majority of which were published between 1852 and 1911.
Each document is approximately the first 2000 words of the novels leading to a total of
210532 tokens in the entire data set. It has multiple layers of annotation, but
here we only focus on the Named Entity and Event annotations. 
To learn about the entity annotations please checkout
[this paper](https://people.ischool.berkeley.edu/~dbamman/pubs/pdf/naacl2019_literary_entities.pdf)
and [this one](https://aclanthology.org/P19-1353.pdf) for the event annotations.

Most config files in [`litbank_pipeline/configs`](litbank_pipeline/configs) project
were generated with an appropriate
[`init config`](https://spacy.io/api/cli#init-config) command.



## 📋 project.yml

The [`project.yml`](project.yml) defines the data assets required by the
project, as well as the available commands and workflows. For details, see the
[spaCy projects documentation](https://spacy.io/usage/projects).

### ⏯ Commands

The following commands are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run).
Commands are only re-run if their inputs have changed.

| Command | Description |
| --- | --- |
| `prepare-entities` | Prepare the LitBank entities for use in spaCy. |
| `prepare-events` | Prepare the LitBank events for use in spaCy. |
| `train` | Train the default NER pipeline. |
| `find-threshold` | Find classifier threshold for spancat. |
| `evaluate` | Evaluate the default NER pipeline on the development set. |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `prepare` | `prepare-entities` &rarr; `prepare-events` |
| `train-pipeline` | `train` &rarr; `evaluate` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/entities/` | Git |  |
| `assets/events/` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
