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
| `train-ner-lstm` | Train the NER pipeline with an LSTM encoder. |
| `train-spancat` | Train the default spancat pipeline. |
| `train-spancat-lstm` | Train the spancat pipeline with an LSTM encoder. |
| `find-threshold` | Find classifier threshold for spancat. |
| `find-threshold-lstm` | Find classifier threshold for the spancat with the LSTM encoder. |
| `train-spancat-singlelabel` | Train the default spancat-singlelabel pipeline. |
| `train-spancat-singlelabel-lstm` | Train the default spancat-singlelabel pipeline with an LSTM encoder. |
| `train-tagger` | Train the default tagger pipeline. |
| `train-tagger-lstm` | Train the default tagger pipeline with an LSTM encoder. |
| `evaluate-tagger-dev` | Evaluate the default tagger pipeline on the development set. |
| `evaluate-tagger-test` | Evaluate the default tagger pipeline on the test set. |
| `evaluate-tagger-lstm-dev` | Evaluate the tagger pipeline with a BiLSTM encoder on the development set. |
| `evaluate-tagger-lstm-test` | Evaluate the tagger pipeline with a BiLSTM encoder on the test set. |
| `evaluate-ner-dev` | Evaluate the default NER pipeline on the development set. |
| `evaluate-ner-test` | Evaluate the default NER pipeline on the test set. |
| `evaluate-ner-lstm-dev` | Evaluate the NER pipeline a BiLSTM encoder on the development set. |
| `evaluate-ner-lstm-test` | Evaluate the NER pipeline with a BiLSTM encoder on the test set. |
| `evaluate-spancat-dev` | Evaluate the default spancat model on the development set. |
| `evaluate-spancat-test` | Evaluate default spancat pipeline on the test set. |
| `evaluate-spancat-lstm-dev` | Evaluate the spancat pipeline with a BiLSTM encoder on the development set. |
| `evaluate-spancat-lstm-test` | Evaluate spancat model with a BiLSTM encoder on the test set. |
| `evaluate-spancat-singlelabel-dev` | Evaluate the default spancat-singlelabel pipeline on the development set. |
| `evaluate-spancat-singlelabel-test` | Evaluate the default spancat-singlelabel pipeline on the test set. |
| `evaluate-spancat-singlelabel-lstm-dev` | Evaluate the spancat-singlelabel pipeline with a BiLSTM encoder on the development set. |
| `evaluate-spancat-singlelabel-lstm-test` | Evaluate the spancat-singlelabel pipeline with a BiLSTM encoder on the test set. |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `ner` | `train-ner` &rarr; `evaluate-ner-test` |
| `ner-lstm` | `train-ner-lstm` &rarr; `evaluate-ner-lstm-test` |
| `spancat` | `train-spancat` &rarr; `evaluate-spancat-test` |
| `spancat-lstm` | `train-spancat-lstm` &rarr; `evaluate-spancat-lstm-test` |
| `spancat-singlelabel` | `train-spancat-singlelabel` &rarr; `evaluate-spancat-singlelabel-test` |
| `spancat-singlelabel-lstm` | `train-spancat-singlelabel-lstm` &rarr; `evaluate-spancat-singlelabel-lstm-test` |
| `tagger` | `train-tagger` &rarr; `evaluate-tagger-test` |
| `tagger-lstm` | `train-tagger-lstm` &rarr; `evaluate-tagger-lstm-test` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/entities/` | Git |  |
| `assets/events/` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->