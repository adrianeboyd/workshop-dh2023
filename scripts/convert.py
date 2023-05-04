from pathlib import Path
from typing import List

import typer
from spacy.tokens import Doc, DocBin, Span, SpanGroup
from spacy.training.converters import conll_ner_to_docs
from wasabi import msg


def convert_iob_to_docs(
    data: str,
    col: str,
    ent_type: str,
) -> List[Doc]:
    """Parse dataset into spaCy docs

    Our strategy here is to reuse the conll -> ner method from spaCy and
    re-apply that n times. We don't want to write our own ConLL/IOB parser.
    """
    header = data[0]
    cols = header.strip().split("\t")
    col_index = cols.index(col)

    # strip comments
    data = data[1:]
    data = [line for line in data if not line.startswith("#")]

    tokens = []
    iobs = []
    docs = []
    for line in data:
        if line.startswith("#"):
            continue
        if line.strip() == "" and len(tokens) > 0:
            conll_data = "".join(["\t".join(x) + "\n" for x in zip(tokens, iobs)])
            doc = list(conll_ner_to_docs(conll_data, no_print=True))[0]
            doc.spans[ent_type] = doc.ents
            docs.append(doc)
            tokens = []
            iobs = []
        elif line.strip() != "":
            cols = line.strip().split("\t")
            tokens.append(cols[0])
            iob = "O"
            if f"B-{ent_type}" in cols[col_index]:
                iob = f"B-{ent_type}"
            if f"I-{ent_type}" in cols[col_index]:
                iob = f"I-{ent_type}"
            iobs.append(iob)
    return docs


def main(
    filepath: Path = typer.Argument(..., exists=True),
    col: str = typer.Argument(...),
    ent_type: str = typer.Argument(...),
    output: Path = typer.Option(..., "-o", "--output", exists=False),
):
    with filepath.open("r", encoding="utf-8") as f:
        data = f.readlines()

    docs = convert_iob_to_docs(data, col, ent_type)
    with msg.loading(f"Saving into DocBin..."):
        doc_bin = DocBin(docs=docs)
        doc_bin.to_disk(output)
        msg.good(f"Saved to {output}")


if __name__ == "__main__":
    typer.run(main)
