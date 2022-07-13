import logging
import re
import warnings
from dataclasses import dataclass
from itertools import chain
from operator import attrgetter
from typing import Optional, Tuple, Union

import spacy
import textdistance
from spacy.matcher import Matcher, PhraseMatcher

logger = logging.getLogger(__name__)


class SimilarityRecognizer:

    similarity = textdistance.cosine.similarity
    default_threshold = 0.7  # seems to work good enough

    def __init__(self, spacy_nlp, intents, threshold=None):
        self.spacy_nlp = spacy_nlp
        self.examples, self.labels = [], []
        for definition in intents:
            self.examples.extend([spacy_nlp.make_doc(e) for e in definition.examples])
            self.labels.extend([definition.name] * len(definition.examples))
        self.threshold = threshold or self.default_threshold

    def _preprocess(self, doc):
        return [t.lower_ for t in doc]

    def __call__(self, doc):
        tokens = self._preprocess(doc)
        scores = [self.similarity(tokens, self._preprocess(example)) for example in self.examples]

        max_scores = {}
        for score, label, example in zip(scores, self.labels, self.examples):
            if score > max_scores.get(label, self.threshold):
                max_scores[label] = score
                logger.debug(f"label {label!r} score {score} example {example.text!r}")

        result = []
        for label, score in max_scores.items():
            confidence = score / len(max_scores)
            result.append(RecognizedIntent(label, confidence))
        return result


def PhraseEntities(spacy_nlp, entities):
    matcher = PhraseMatcher(spacy_nlp.vocab, attr="LOWER")
    ids = {}
    for entity in entities:
        for value in entity.values:
            key = f"{entity.name}-{value.name}"
            match_id = spacy_nlp.vocab.strings.add(key)
            ids[match_id] = (entity.name, value.name)
            patterns = list(spacy_nlp.pipe(value.phrases))
            matcher.add(key, patterns)

    def phrase_entities(doc):
        for match_id, start, end in matcher(doc):
            name, value = ids[match_id]
            span = doc[start:end]
            # TODO deal with entities overlap
            yield RecognizedEntity.from_span(span, name, value)

    return phrase_entities


def RegexpEntities(spacy_nlp, entities):
    regexps = []
    for entity in entities:
        for value in entity.values:
            for regexp in value.regexps:
                regexps.append(
                    {
                        "label": entity.name,
                        "id": value.name,
                        "pattern": re.compile(regexp),
                    }
                )

    def regexp_entities(doc):
        for p in regexps:
            for match in re.finditer(p["pattern"], doc.text):
                start, end = match.span()
                if start == end:
                    continue
                yield RecognizedEntity(
                    name=p["label"],
                    value=p["id"],
                    literal=doc.text[start:end],
                    start_char=start,
                    end_char=end,
                )

    return regexp_entities


def SpacyMatcherEntities(spacy_nlp):

    from number_parser import parse_number

    matcher = Matcher(spacy_nlp.vocab)
    matcher.add("number", [[{"LIKE_NUM": True, "OP": "+"}]], greedy="LONGEST")
    matcher.add("email", [[{"LIKE_EMAIL": True}]])
    matcher.add("url", [[{"LIKE_URL": True}]])

    def spacy_matcher_entities(doc):
        matches = matcher(doc, as_spans=True)
        # does spacy reverse the order while matching greedly?
        matches = sorted(matches, key=attrgetter("start"))
        for span in matches:
            if span.label_ == "number":
                number = parse_number(span.text)
                yield RecognizedEntity.from_span(span, "number", number)
            else:
                yield RecognizedEntity.from_span(span)

    return spacy_matcher_entities


def DateParserEntities():
    """
    Date/Time parsing just for pet projects.
    Use duckling for full featured date/time recognition support.
    """

    from dateparser import parse
    from dateparser.date import DateDataParser
    from dateparser.search import search_dates

    # language autodetection slows down the parser
    # provide language explicitly

    ddp = DateDataParser(languages=["en"], settings={"RETURN_TIME_AS_PERIOD": True})

    def dateparser_entities(doc):
        # suppress known PytzUsageWarning from dateparser
        with warnings.catch_warnings():
            warnings.simplefilter("ignore")

            shift = 0
            results = search_dates(doc.text, languages=["en"])
            if results is None:
                return
            for literal, dt in results:
                start_char = doc.text.index(literal, shift)
                end_char = start_char + len(literal)
                shift = end_char
                # a bit tricky way to split date and time parts
                dd = ddp.get_date_data(literal)
                if dd.period == "time":
                    if parse(literal, languages=["en"], settings={"REQUIRE_PARTS": ["day"]}):
                        yield RecognizedEntity(
                            "date", dt.date().isoformat(), literal, start_char, end_char
                        )
                    yield RecognizedEntity(
                        "time", dt.time().isoformat(), literal, start_char, end_char
                    )
                else:
                    yield RecognizedEntity(
                        "date", dt.date().isoformat(), literal, start_char, end_char
                    )

    return dateparser_entities


def RuleBasedEntities(spacy_nlp):
    """
    FIXME: need some generic way to resolve overlaps
    Need to manually compose because date/time entities could not overlap with number entities
    """
    dateparser_entities = DateParserEntities()
    spacy_matcher_entities = SpacyMatcherEntities(spacy_nlp)

    def rule_based_entities(doc):
        seen_chars = set()
        for entity in dateparser_entities(doc):
            seen_chars.update(range(entity.start_char, entity.end_char))
            yield entity
        for entity in spacy_matcher_entities(doc):
            if entity.name == "number" and (
                entity.start_char in seen_chars or entity.end_char - 1 in seen_chars
            ):
                continue
            yield entity

    return rule_based_entities


@dataclass(frozen=True)
class RecognizedIntent:

    name: str
    confidence: float


@dataclass(frozen=True)
class IntentsContext:

    top: Optional[RecognizedIntent]
    ranking: Tuple[RecognizedIntent]

    def __getattr__(self, name):
        if self.top and self.top.name == name:
            return self.top
        return None


@dataclass(frozen=True)
class RecognizedEntity:

    name: str
    value: Union[str, int]
    literal: str
    start_char: int
    end_char: int

    @classmethod
    def from_span(cls, span, name=None, value=None):
        if value is None:
            value = span.text
        return cls(name or span.label_, value, span.text, span.start_char, span.end_char)


@dataclass(frozen=True)
class EntitiesProxy:

    first: RecognizedEntity
    all_objects: Tuple[RecognizedEntity]

    @property
    def all_values(self):
        return tuple(e.value for e in self.all_objects)

    def __getattr__(self, name):
        """
        Convenient access in expressions
            entities.menu.value == entities.menu.first.value
            entities.menu.literal == entities.menu.first.literal
        and
            entities.menu.vegetarian == ('vegetarian' in entities.menu.all_values)
        """
        if hasattr(self.first, name):
            return getattr(self.first, name)
        return name in self.all_values


@dataclass(frozen=True)
class EntitiesContext:

    proxies: dict[str, EntitiesProxy]
    all_objects: Tuple[RecognizedEntity]

    def __getattr__(self, name):
        """
        Convenient access in expressions
            entities.menu == entities.proxies.get('menu')
        """
        return self.proxies.get(name)


class Nlu:
    @classmethod
    def from_definitions(cls, definitions):
        spacy_nlp = spacy.blank("en")

        config = vars(definitions.services.similarity_recognizer)
        intent_recognizer = SimilarityRecognizer(spacy_nlp, definitions.intents, **config)

        entity_recognizers = [
            PhraseEntities(spacy_nlp, definitions.entities),
            RegexpEntities(spacy_nlp, definitions.entities),
            RuleBasedEntities(spacy_nlp),
        ]

        config = vars(definitions.services.nlu)
        return cls(spacy_nlp, intent_recognizer, entity_recognizers, **config)

    default_threshold = 0.5  # standard probability threshold

    def __init__(self, spacy_nlp, intent_recognizer, entity_recognizers, threshold=None):
        self.spacy_nlp = spacy_nlp
        self.intent_recognizer = intent_recognizer
        if not isinstance(entity_recognizers, list):
            entity_recognizers = [entity_recognizers]
        self.entity_recognizers = entity_recognizers
        self.threshold = threshold or self.default_threshold

    def __call__(self, message):
        doc = self.spacy_nlp(message.text)
        intents = self._resolve_intents(self.intent_recognizer(doc))
        entities = self._resolve_entities(
            list(
                chain.from_iterable(recognizer(doc=doc) for recognizer in self.entity_recognizers)
            )
        )
        return intents, entities

    def _resolve_intents(self, recognized_intents):
        ranking = tuple(sorted(recognized_intents, key=attrgetter("confidence"), reverse=True))
        for intent in ranking:
            logger.debug(f"{intent}")
        top = ranking[0] if ranking else None
        if top and top.confidence < self.threshold:
            top = None
        return IntentsContext(top, ranking)

    def _resolve_entities(self, recognized_entities):
        mapping = {}
        for entity in recognized_entities:
            logger.debug(f"{entity}")
            mapping.setdefault(entity.name, list()).append(entity)
        proxies = {}
        for name, objects in mapping.items():
            proxies[name] = EntitiesProxy(objects[0], tuple(objects))
        return EntitiesContext(proxies, tuple(recognized_entities))
