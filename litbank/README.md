<!-- SPACY PROJECT: AUTO-GENERATED DOCS START (do not remove) -->

# 🪐 spaCy Project: Train spancat pipelines on LitBank entity annotations.

Train CNN and TRF pipelines on LitBank entity annotation comparing n-gram, subtree, and span finder suggesters.


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
| `download-lg` | Download lg pipeline for vectors and subtree suggester |
| `download-trf` | Download trf pipeline subtree suggester |
| `train-spancat_ngram_lg` |  |
| `evaluate-spancat_ngram_lg` |  |
| `package-spancat_ngram_lg` |  |
| `train-spancat_span_finder_lg` |  |
| `evaluate-spancat_span_finder_lg` |  |
| `package-spancat_span_finder_lg` |  |
| `train-spancat_subtree_lg` |  |
| `evaluate-spancat_subtree_lg` |  |
| `package-spancat_subtree_lg` |  |
| `train-spancat_ngram_trf` |  |
| `evaluate-spancat_ngram_trf` |  |
| `package-spancat_ngram_trf` |  |
| `train-spancat_subtree_trf` |  |
| `evaluate-spancat_subtree_trf` |  |
| `package-spancat_subtree_trf` |  |
| `train-spancat_span_finder_trf` |  |
| `evaluate-spancat_span_finder_trf` |  |
| `package-spancat_span_finder_trf` |  |

### ⏭ Workflows

The following workflows are defined by the project. They
can be executed using [`spacy project run [name]`](https://spacy.io/api/cli#project-run)
and will run the specified commands in order. Commands are only re-run if their
inputs have changed.

| Workflow | Steps |
| --- | --- |
| `prepare` | `prepare-entities` &rarr; `download-lg` &rarr; `download-trf` |
| `ngram_lg` | `train-spancat_ngram_lg` &rarr; `evaluate-spancat_ngram_lg` &rarr; `package-spancat_ngram_lg` |
| `train-all` | `train-spancat_ngram_lg` &rarr; `evaluate-spancat_ngram_lg` &rarr; `train-spancat_subtree_lg` &rarr; `evaluate-spancat_subtree_lg` &rarr; `train-spancat_span_finder_lg` &rarr; `evaluate-spancat_span_finder_lg` &rarr; `train-spancat_ngram_trf` &rarr; `evaluate-spancat_ngram_trf` &rarr; `train-spancat_subtree_trf` &rarr; `evaluate-spancat_subtree_trf` &rarr; `train-spancat_span_finder_trf` &rarr; `evaluate-spancat_span_finder_trf` |
| `package-all` | `package-spancat_ngram_lg` &rarr; `package-spancat_subtree_lg` &rarr; `package-spancat_span_finder_lg` &rarr; `package-spancat_ngram_trf` &rarr; `package-spancat_subtree_trf` &rarr; `package-spancat_span_finder_trf` |

### 🗂 Assets

The following assets are defined by the project. They can
be fetched by running [`spacy project assets`](https://spacy.io/api/cli#project-assets)
in the project directory.

| File | Source | Description |
| --- | --- | --- |
| `assets/entities/` | Git |  |

<!-- SPACY PROJECT: AUTO-GENERATED DOCS END (do not remove) -->
