| Notebook                                                                                                        | Description                      |
| --------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| [`01_intro_to_spacy`][01_intro_to_spacy]<br />[![Open in Colab][colab]][01_intro_to_spacy_colab]                | Intro to spaCy                   |
| [`02_spancat`][02_spancat]<br />[![Open in Colab][colab]][02_spancat_colab]                                     | Intro to spancat                 |
| [`03_litbank_data`][03_litbank_data]<br />[![Open in Colab][colab]][03_litbank_data_colab]                      | Inspect litbank spans data       |
| [`04_litbank_training`][04_litbank_training]<br />[![Open in Colab][colab]][04_litbank_training_colab]          | Train litbank spancat pipeline   |
| [`05_litbank_pipelines`][05_litbank_pipelines]<br />[![Open in Colab][colab]][05_litbank_pipelines_colab]       | Run litbank spancat pipeline     |
| [`06_unsilence_data`][06_unsilence_data]<br />[![Open in Colab][colab]][06_unsilence_data_colab]                | Inspect unsilence spans data     |
| [`07_unsilence_training`][07_unsilence_training]<br />[![Open in Colab][colab]][07_unsilence_training_colab]    | Train unsilence spancat pipeline |
| [`08_unsilence_pipelines`][08_unsilence_pipelines]<br />[![Open in Colab][colab]][08_unsilence_pipelines_colab] | Run unsilence spancat pipeline   |

[colab]:
  https://gistcdn.githack.com/ines/dcf354aa71a7665ae19871d7fd14a4e0/raw/461fc1f61a7bc5860f943cd4b6bcfabb8c8906e7/colab-badge.svg
[01_intro_to_spacy]: 01_intro_to_spacy.ipynb
[01_intro_to_spacy_colab]:
  https://colab.research.google.com/github/adrianeboyd/workshop-dh2023/blob/main/notebooks/01_intro_to_spacy.ipynb
[02_spancat]: 02_spancat.ipynb
[02_spancat_colab]:
  https://colab.research.google.com/github/adrianeboyd/workshop-dh2023/blob/main/notebooks/02_spancat.ipynb
[03_litbank_data]: 03_litbank_data.ipynb
[03_litbank_data_colab]:
  https://colab.research.google.com/github/adrianeboyd/workshop-dh2023/blob/main/notebooks/03_litbank_data.ipynb
[04_litbank_training]: 04_litbank_training.ipynb
[04_litbank_training_colab]:
  https://colab.research.google.com/github/adrianeboyd/workshop-dh2023/blob/main/notebooks/04_litbank_training.ipynb
[05_litbank_pipelines]: 05_litbank_pipelines.ipynb
[05_litbank_pipelines_colab]:
  https://colab.research.google.com/github/adrianeboyd/workshop-dh2023/blob/main/notebooks/05_litbank_pipelines.ipynb
[06_unsilence_data]: 06_unsilence_data.ipynb
[06_unsilence_data_colab]:
  https://colab.research.google.com/github/adrianeboyd/workshop-dh2023/blob/main/notebooks/06_unsilence_data.ipynb
[07_unsilence_training]: 07_unsilence_training.ipynb
[07_unsilence_training_colab]:
  https://colab.research.google.com/github/adrianeboyd/workshop-dh2023/blob/main/notebooks/07_unsilence_training.ipynb
[08_unsilence_pipelines]: 08_unsilence_pipelines.ipynb
[08_unsilence_pipelines_colab]:
  https://colab.research.google.com/github/adrianeboyd/workshop-dh2023/blob/main/notebooks/08_unsilence_pipelines.ipynb




## How to get started locally?
If you don't have any experience with setting up git repositories and python/jupyter locally, your best option might be using the colab link. The following script is meant for users who know the basics and just need a reminder of all steps that are (potentially) necessary and which they can adapt for their needs.
```bash
PATH_TO_PYTHON=/opt/homebrew/bin/python3.10
PATH_TO_VIRTUAL_ENVS=/Users/USER/envs/
KERNEL_NAME=wdh23

# 1. clone repo and change to notebook directory
git clone https://github.com/adrianeboyd/workshop-dh2023.git
cd workshop-dh2023
cd notebooks

# 2. create virtual environment and activate it
$PATH_TO_PYTHON -m venv ${PATH_TO_VIRTUAL_ENVS}workshop-dh2023
source  ${PATH_TO_VIRTUAL_ENVS}workshop-dh2023/bin/activate

# 3. Install jupyter and add current environment as ipy kernel
pip install jupyter
python -m ipykernel install --user --name $KERNEL_NAME

# 4. start notebook. When opening a notebook, select Kernel > Change Kernel > $KERNEL_NAME
jupyter notebook
```
