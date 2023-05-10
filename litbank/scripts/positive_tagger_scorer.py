from typing import Iterable, Any, Dict, Set

from spacy.scorer import PRFScore, MISSING_VALUES
from spacy.training.example import Example
from spacy.util import registry


def score_positive_tagger(
    examples: Iterable[Example],
    positive: str,
    *,
    missing_values: Set[Any] = MISSING_VALUES,  # type: ignore[assignment]
    **cfg,
) -> Dict[str, Any]:
    """Returns an accuracy score for token level classification
    only for the positive class.
    Modified from spacy.scorer.Scorer.score_token_attr.

    examples (Iterable[Example]): Examples to score
    missing_values (Set[Any]): Attribute values to treat as missing annotation
        in the reference annotation.
    RETURNS (Dict[str, Any]): A dictionary containing the accuracy score
        under the key attr_acc.
    """
    tag_score = PRFScore()
    for example in examples:
        gold_doc = example.reference
        pred_doc = example.predicted
        align = example.alignment
        gold_tags = set()
        discard = set()
        for gold_i, token in enumerate(gold_doc):
            value = token.tag_
            if value not in missing_values and value == positive:
                gold_tags.add((gold_i, value))
            else:
                discard.add(gold_i)
        pred_tags = set()
        for token in pred_doc:
            if token.orth_.isspace():
                continue
            if align.x2y.lengths[token.i] == 1:
                gold_i = align.x2y[token.i][0]
                if gold_i not in discard:
                    pred_tags.add((gold_i, token.tag_))
        tag_score.score_set(pred_tags, gold_tags)
    score_key = "positive_acc"
    if len(tag_score) == 0:
        return {score_key: None}
    else:
        return {score_key: tag_score.fscore}


@registry.scorers("spacy.positive_tagger_scorer.v1")
def make_positive_scorer(positive: str):
    def positive_scorer(examples, **kwargs):
        return score_positive_tagger(examples, positive, **kwargs)
    return positive_scorer
