import random
from typing import Sequence, Any, Optional, Tuple, List
from math import ceil

import spacy
from spacy.tokens import DocBin
from spacy.util import ensure_path, filter_spans
from radicli import Radicli, Arg
from wasabi import msg


cli = Radicli(
    help=(
        "I am a small radicli app that preprocesses "
        "a data set in brat format data set for use in spaCy. "
    )
)


def _train_dev_test_split(
    data: Sequence[Any],
    train_ratio: float,
    dev_ratio: float,
    shuffle: Optional[bool] = False,
    seed: Optional[int] = None,
) -> Tuple[List[Any], List[Any], List[Any]]:
    """
    Split data into training, development and test portions.
    If 'shuffle' is true then create a random split. The
    number of samples in each portion is controlled by the
    'train_ratio' and 'dev_ratio' parameters.
    """
    if shuffle:
        if not seed:
            raise ValueError("Must provide 'seed' when 'shuffle = True'")
        rng = random.Random(seed)
        rng.shuffle(data)
    n_samples = len(data)
    test_ratio = 1.0 - (train_ratio + dev_ratio)
    n_test = ceil(test_ratio * n_samples)
    n_dev = ceil(dev_ratio * n_samples)
    n_train = n_samples - (n_test + n_dev)
    train = data[:n_train]
    dev = data[n_train:n_train + n_dev]
    test = data[n_train + n_dev:]
    return train, dev, test


@cli.command(
    "prepare-brat",
    input_dir=Arg("--input-dir", "-i", help="Path to .txt and .ann files."),
    output_file=Arg("--output-file", "-o", help="Path to write .spacy file."),
    lang=Arg("--lang", "-l", help="Language of the dataset"),
    force=Arg("--force", "-f", help="Force overwrite output_file if exists.")
)
def prepare_brat(
    input_dir: str,
    output_file: str,
    lang: str,
    force: bool
) -> None:
    docbin = DocBin()
    nlp = spacy.blank(lang)
    input_dir = ensure_path(input_dir)
    output_file = ensure_path(output_file)
    if not input_dir.exists():
        msg.warn(f"Could not find {input_dir}.", exits=1)
    if not input_dir.is_dir():
        raise msg.warn("'input_dir' must be a directory.", exits=1)
    if output_file.exists() and not force:
        raise msg.warn(
            f"{output_file} already exists. "
            "Use the -f or --force option to overwrite it.",
            exits=1
        )
    if output_file.is_dir():
        raise msg.warn("'output_file' cannot be a directory.", exits=1)
    documents = 0
    for path in input_dir.iterdir():
        if path.suffix not in [".ann", ".txt"]:
            msg.warn(
                "Does not seem to be a brat annotation directory. "
                "Make sure directory only contains .ann and .txt files.",
                exits=1
            )
        if path.suffix == ".txt":
            text = path.read_text(encoding="utf8")
            ann_path = (input_dir / (path.stem + '.ann'))
            if not ann_path.exists():
                msg.warn(f"Did not file annotation for {path}.")
                continue
            annotations = ann_path.read_text(encoding="utf8").split('\n')
            doc = nlp(text)
            spans = []
            for line in annotations[:-1]:
                if line.startswith("#"):
                    continue
                label, start, end = line.split('\t')[1].split()
                span = doc.char_span(
                    int(start), int(end), label=label, alignment_mode="expand"
                )
                spans.append(span)

            doc.spans["sc"] = spans
            docbin.add(doc)
            documents += 1
    docbin.to_disk(output_file)
    msg.good(f"Found {documents} and written DocBin to {output_file}")


@cli.command(
    "split",
    input_file=Arg("--input-file", "-i", help="Path to write .spacy file."),
    lang=Arg("--lang", "-l", help="Language of the dataset."),
    train_ratio=Arg("--train-ratio", "-t", help="Language of the dataset"),
    dev_ratio=Arg("--dev-ratio", "-d", help="Force overwrite output_file if exists."),
    shuffle=Arg("--shuffle", "-sh", help="Shuffle input docs before splitting."),
    seed=Arg("--seed", "-se", help="Random seed for shuffling.")
)
def split(
    input_file: str,
    lang: str,
    train_ratio: float,
    dev_ratio: float,
    shuffle: bool,
    seed: int
) -> None:
    input_file = ensure_path(input_file)
    if input_file.is_dir():
        raise msg.warn(
            "'input_file' should be a file not a directory.", exits=1
        )
    if not input_file.exists():
        raise msg.warn(f"Could not find {input_file}.", exits=1)
    if not (0 < train_ratio < 1.0):
        raise msg.warn(
            f"'train_ratio' has to be between "
            f"0.0 and 1.0, but found {train_ratio}.",
            exits=1
        )
    if not (0 < dev_ratio < 1.0):
        raise msg.warn(
            f"'dev_ratio' has to be between "
            f"0.0 and 1.0, but found {dev_ratio}.",
            exits=1
        )
    if not (train_ratio + dev_ratio < 1.0):
        raise msg.warn(
            "The sum of 'train_ratio' has to be less than 1.0 "
            "to leave room for the test set. "
            f"Found `train_ratio`: {train_ratio} and `dev_ratio`: {dev_ratio} "
            f"whose sum is {train_ratio + dev_ratio}.",
            exits=1
        )
    nlp = spacy.blank(lang)
    db = DocBin().from_disk(input_file)
    docs = list(db.get_docs(nlp.vocab))
    msg.info(f"Found {len(docs)} docs in {input_file}")
    train, dev, test = _train_dev_test_split(
        docs, train_ratio, dev_ratio, shuffle, seed
    )
    datasets = {"train": train, "dev": dev, "test": test}
    msg.text(
        f"Done splitting the train ({len(train)}), dev ({len(dev)}), "
        f" and test ({len(test)}) datasets!"
    )
    for dataset, docs in datasets.items():
        file_name = f"{input_file.stem}-{dataset}.spacy"
        output_path = input_file.parents[0] / file_name
        db_new = DocBin(docs=docs)
        db_new.to_disk(output_path)
        msg.good(f"Saved {dataset} ({len(docs)}) dataset to {output_path}")


@cli.command(
    "spans2ents",
    input_file=Arg("--input-file", "-i", help="Path to .spacy file."),
    output_file=Arg("--output-file", "-o", help="Path to write .spacy file."),
    span_key=Arg("--span-key", "-s", help="Span key to transfer to ents."),
    lang=Arg("--lang", "-l", help="Language of the dataset."),
    force=Arg("--force", "-f", help="Force overwrite output_file if exists.")
)
def spans2ents(
    input_file: str,
    output_file: str,
    span_key: str,
    lang: str,
    force: bool
) -> None:
    input_file = ensure_path(input_file)
    output_file = ensure_path(output_file)
    if not input_file.exists():
        msg.warn(f"Could not find {input_file}.", exits=1)
    if input_file.is_dir():
        raise msg.warn(
            "'input_dir' should be a file not a directory.", exits=1
        )
    if not output_file.exists() and not force:
        raise msg.warn(
            f"{output_file} already exists. "
            "Use the -f or --force option to overwrite it.",
            exits=1
        )
    nlp = spacy.blank(lang)
    db = DocBin().from_disk(input_file)
    newdb = DocBin()
    docs = list(db.get_docs(nlp.vocab))
    msg.good(f"Loaded {len(docs)}.")
    filtered = 0
    total = 0
    for doc in docs:
        spans = list(filter_spans(doc.spans[span_key]))
        filtered += len(doc.spans[span_key]) - len(spans)
        total += len(doc.spans[span_key])
        doc.set_ents(spans)
        newdb.add(doc)
    msg.info(
        f"Out of total {total} spans {filtered} were "
        f"filtered out. Kept {total - filtered}."
    )
    newdb.to_disk(output_file)


@cli.command(
    "spans2tags",
    input_file=Arg("--input-file", "-i", help="Path to .spacy file."),
    output_file=Arg("--output-file", "-o", help="Path to write .spacy file."),
    span_key=Arg("--span-key", "-s", help="Span key to transfer to ents."),
    lang=Arg("--lang", "-l", help="Language of the dataset."),
    force=Arg("--force", "-f", help="Force overwrite output_file if exists.")
)
def spans2tags(
    input_file: str,
    output_file: str,
    span_key: str,
    lang: str,
    force: bool
) -> None:
    input_file = ensure_path(input_file)
    output_file = ensure_path(output_file)
    if not input_file.exists():
        msg.warn(f"Could not find {input_file}.", exits=1)
    if input_file.is_dir():
        raise msg.warn(
            "'input_dir' should be a file not a directory.", exits=1
        )
    if not output_file.exists() and not force:
        raise msg.warn(
            f"{output_file} already exists. "
            "Use the -f or --force option to overwrite it.",
            exits=1
        )
    nlp = spacy.blank(lang)
    db = DocBin().from_disk(input_file)
    newdb = DocBin()
    docs = list(db.get_docs(nlp.vocab))
    msg.good(f"Loaded {len(docs)}.")
    filtered = 0
    total = 0
    for doc in docs:
        spans = list(filter_spans(doc.spans[span_key]))
        idxs = {span.start: span.label_ for span in spans if len(span) == 1}
        for token in doc:
            idx = token.i
            if idx in idxs:
                token.tag_ = idxs[idx]
            else:
                token.tag_ = "O"
        filtered += len(doc.spans[span_key]) - len(idxs)
        total += len(doc.spans[span_key])
        newdb.add(doc)
    msg.info(
        f"Out of total {total} spans {filtered} were "
        f"filtered out. Kept {total - filtered}."
    )
    newdb.to_disk(output_file)


if __name__ == "__main__":
    cli.run()
