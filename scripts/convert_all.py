from pathlib import Path
from typing import List

import typer
from spacy.tokens import Doc, DocBin, Span
from spacy.training.converters import conll_ner_to_docs
from wasabi import msg


def convert_iob_to_docs(
    data: str,
    col: str,
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
    data = [line.strip() for line in data if not line.startswith("#")]

    tokens = []
    iobs = []
    docs = []
    # get all ent types in advance
    ent_types = set()
    for line in data:
        if line != "":
            cols = line.split("\t")
            if cols[col_index] != "O":
                for ent in cols[col_index].split(","):
                    ent_types.add(ent[2:])
    for line in data:
        if line.strip() == "" and len(tokens) > 0:
            doc = list(
                conll_ner_to_docs(
                    "".join(
                        "\t".join(x) + "\n" for x in zip(tokens, ["O"] * len(tokens))
                    ),
                    no_print=True,
                )
            )[0]
            doc.spans[col] = []
            for ent_type in ent_types:
                ent_type_iobs = ["O"] * len(tokens)
                for i, ent in enumerate(iobs):
                    iob_values = ent.split(",")
                    for iob_value in iob_values:
                        if ent_type in iob_value:
                            ent_type_iobs[i] = iob_value
                conll_data = "".join(
                    ["\t".join(x) + "\n" for x in zip(tokens, ent_type_iobs)]
                )
                ent_type_doc = list(conll_ner_to_docs(conll_data, no_print=True))[0]
                doc.spans[col] += [
                    Span(doc, e.start, e.end, e.label_) for e in ent_type_doc.ents
                ]
            docs.append(doc)
            tokens = []
            iobs = []
        elif line.strip() != "":
            cols = line.strip().split("\t")
            tokens.append(cols[0])
            iobs.append(cols[col_index])
    return docs


def main(
    filepath: Path = typer.Argument(..., exists=True),
    col: str = typer.Argument(...),
    output: Path = typer.Option(..., "-o", "--output", exists=False),
):
    with filepath.open("r", encoding="utf-8") as f:
        data = f.readlines()

    docs = convert_iob_to_docs(data, col)
    with msg.loading("Saving into DocBin..."):
        doc_bin = DocBin(docs=docs)
        doc_bin.to_disk(output)
        msg.good(f"Saved to {output}")


if __name__ == "__main__":
    typer.run(main)
