<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Train NER/spancat on UnSilence VOC

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
| `download-vectors` | Download and install Dutch floret vectors |
| `convert-data-ner` | Prepare the NER per type data for spaCy |
| `convert-data-spans` | Prepare the spans data for spaCy |
| `train-ner` | Train NER per-type pipelines. |
| `train-ner-trf` | Train NER TRF per type. |
| `evaluate-ner` | Evaluate the NER CNN pipelines |
| `evaluate-ner-trf` | Evaluate the NER TRF pipelines |
| `train-spancat` | Train the default spancat pipeline. |
| `train-spancat-trf` | Train spancat TRF |
| `evaluate-spancat` | Evaluate the spancat CNN pipeline |
| `evaluate-spancat-trf` | Evaluate the spancat TRF pipeline |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `download` | `download-vectors` |
| `convert` | `convert-data-ner` &rarr; `convert-data-spans` |
| `ner` | `train-ner` &rarr; `evaluate-ner` &rarr; `train-ner-trf` &rarr; `evaluate-ner-trf` |
| `spancat` | `train-spancat` &rarr; `evaluate-spancat` &rarr; `train-spancat-trf` &rarr; `evaluate-spancat-trf` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/UnSilence_VOC` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
