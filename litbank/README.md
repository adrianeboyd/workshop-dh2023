<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Train NER and event trigger detection pipelines on LitBank.

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
| `prepare-event` | Prepare the LitBank events for use in spaCy. |
| `train-ner` | Train the default NER pipeline. |
| `train-ner-trf` | Train the ner pipeline with an transformer encoder. |
| `train-spancat` | Train the default spancat pipeline. |
| `train-spancat-trf` | Train the spancat pipeline with an transformer encoder. |
| `find-threshold` | Find classifier threshold for spancat. |
| `train-spancat-singlelabel` | Train the default spancat-singlelabel pipeline. |
| `train-tagger` | Train the default tagger pipeline. |
| `evaluate-tagger-dev` | Evaluate the default tagger pipeline on the development set. |
| `evaluate-tagger-test` | Evaluate the default tagger pipeline on the test set. |
| `evaluate-ner-dev` | Evaluate the default NER pipeline on the development set. |
| `evaluate-ner-test` | Evaluate the default NER pipeline on the test set. |
| `evaluate-spancat-dev` | Evaluate the default spancat model on the development set. |
| `evaluate-spancat-test` | Evaluate default spancat pipeline on the test set. |
| `evaluate-spancat-trf-dev` | Evaluate the spancat pipeline with transformer encoder on the development set. |
| `evaluate-spancat-trf-test` | Evaluate spancat model with a transformer encoder on the test set. |
| `evaluate-spancat-singlelabel-dev` | Evaluate the default spancat-singlelabel pipeline on the development set. |
| `evaluate-spancat-singlelabel-test` | Evaluate the default spancat-singlelabel pipeline on the test set. |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `ner` | `train-ner` &rarr; `evaluate-ner-test` |
| `spancat` | `train-spancat` &rarr; `evaluate-spancat-test` |
| `spancat-trf` | `train-spancat-trf` &rarr; `evaluate-spancat-trf-test` |
| `spancat-singlelabel` | `train-spancat-singlelabel` &rarr; `evaluate-spancat-singlelabel-test` |
| `tagger` | `train-tagger` &rarr; `evaluate-tagger-test` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/entities/` | Git |  |
| `assets/events/` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->