import re

from spacy.language import Language
from spacy.pipeline.entityruler import EntityRuler
from spacy.tokens import Doc, Span


@Language.factory(
    "sentex",
    default_config={
        "sentence_regex": "",
        "ignore_regex": "",
        "annotate_ents": False,
        "label": "Sentex",
    },
)
def create_sentex_component(
    nlp: Language,
    name: str,
    sentence_regex: str,
    ignore_regex: str,
    annotate_ents: bool,
    label: str,
):
    return Sentex(nlp, sentence_regex, ignore_regex, annotate_ents, label)


class Sentex:
    """
    Sentex is a spaCy pipeline component that adds spans to the list `Doc._.sentex`
    based on regular expression matches within each sentence of the document. If an
    `ignore_regex` is given, sentences matching that regular expression will be ignored.

    nlp: `Language`,
        A required argument for spacy to use this as a factory
    sentence_regex : `str`,
        A regular expression to match spans within each sentence of the document.
    ignore_regex : `str`,
        A regular expression to identify sentences that should be ignored.
    annotate_ents: `bool`,
        Write/overwrite matches to Doc.ents
    label: `str`,
        If annotate_ents == True, the label for the matched entity
    """

    def __init__(
        self,
        nlp: Language,
        sentence_regex: str,
        ignore_regex: str,
        annotate_ents: bool,
        label: str,
    ):
        self.sentence_regex = sentence_regex
        self.ignore_regex = ignore_regex
        self.annotate_ents = annotate_ents
        self.label = label

        if not Doc.has_extension("sentex"):
            Doc.set_extension("sentex", default=[])

    def __call__(self, doc: Doc) -> Doc:

        for sent in doc.sents:
            should_ignore = bool(re.search(self.ignore_regex, sent.text))
            if should_ignore:
                continue
            for match in re.finditer(self.sentence_regex, sent.text):
                start, end = match.span()
                span = sent.char_span(start, end)
                if span is not None:
                    doc._.sentex.append(span)
        if self.annotate_ents:
            self.set_annotations(doc)
        return doc

    def set_annotations(self, doc):
        """Modify the document in place. Logic taken from spacy.pipeline.entityruler.EntityRuler"""
        entities = list(doc.ents)
        new_entities = []
        seen_tokens = set()
        matches = self._get_matches(doc)
        for match_id, start, end in matches:
            # check for end - 1 here because boundaries are inclusive
            if start not in seen_tokens and end - 1 not in seen_tokens:
                span = Span(doc, start, end, label=match_id)
                new_entities.append(span)
                entities = [
                    e for e in entities if not (e.start < end and e.end > start)
                ]
                seen_tokens.update(range(start, end))
        doc.ents = entities + new_entities

    def _get_matches(self, doc: Doc):
        return [(self.label, m.start, m.end) for m in doc._.sentex]
