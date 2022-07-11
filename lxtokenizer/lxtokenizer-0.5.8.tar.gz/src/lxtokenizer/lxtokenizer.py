import logging
import re
import os
import os.path
import platform


from lxcommon import (
    LxParagraph,
    LxSentence,
    LxToken,
    CintilFormatSpec,
)
import lxcommon.utils
from toolwrapper import ToolWrapper
from openfile import openfile


LOG = logging.getLogger(__name__)


class LxTokenizer(ToolWrapper):
    """A class for tokenizing Portuguese text."""

    TOKENIZER_DIR = os.path.join(os.path.dirname(__file__), "tokenizer")
    TOKENIZER_BIN = os.path.join(TOKENIZER_DIR, platform.machine(), "tokenizer")
    ABBREVS_PATH = os.path.join(TOKENIZER_DIR, "abbrevs.txt")
    CLITICS_PATH = os.path.join(TOKENIZER_DIR, "clitics.txt")
    CONTRS_PATH = os.path.join(TOKENIZER_DIR, "contrs.txt")

    ARGV = [
        TOKENIZER_BIN,
        ABBREVS_PATH,
        CLITICS_PATH,
        CONTRS_PATH,
    ]

    OPEN_QUOTES = "“‘«"
    CLOSE_QUOTES = "”’»"
    QUOTES = OPEN_QUOTES + CLOSE_QUOTES
    QUOTES_RE = re.compile(f"((?:^\\\\\\*)?[{QUOTES}](?:\\*/$)?)")
    CINTIL_FORMAT_SPEC = CintilFormatSpec(tokenized=True)

    @staticmethod
    def _separate_quotes(original_form):
        """this method is a workaround for a bug in the flex-based tokenizer"""
        forms = [form for form in LxTokenizer.QUOTES_RE.split(original_form) if form]
        if len(forms) > 1:
            if forms[0] in LxTokenizer.OPEN_QUOTES:
                forms[0] = "\\*" + forms[0]
            if forms[-1] in LxTokenizer.CLOSE_QUOTES:
                forms[-1] = forms[-1] + "*/"
        return forms

    @staticmethod
    def _separate_slashes(original_form):
        """this method is a workaround for a bug in the flex-based tokenizer"""
        form = original_form
        if form.startswith("\\*"):
            prefix = "\\*"
            form = form[2:]
        else:
            prefix = ""
        if original_form.endswith("*/"):
            suffix = "*/"
            form = form[:-2]
        else:
            suffix = ""
        return (prefix + form.replace("/", " / ").strip() + suffix).split()

    @staticmethod
    def _create_tokens(forms):
        return [
            LxToken.from_cintil(form, LxTokenizer.CINTIL_FORMAT_SPEC)
            for form in forms
        ]

    def __init__(self):
        super().__init__(LxTokenizer.ARGV)
        self.contractions = LxTokenizer._load_contractions()

    @staticmethod
    def _load_contractions():
        contractions = dict()
        # first let's load contracted clitics
        for file_path in LxTokenizer.CLITICS_PATH, LxTokenizer.CONTRS_PATH:
            with openfile(file_path) as lines:
                lines = map(str.strip, lines)
                contracted, expanded = None, None
                for line in lines:
                    if not line or line.startswith("%%"):
                        continue
                    if line.endswith(","):
                        contracted = line[:-1]
                        expanded = None
                    elif line.endswith(";"):
                        expanded = " ".join(
                            [
                                token[:-1] if token.endswith("_") else token
                                for token in line[:-1].split()
                            ]
                        )
                        if contracted and expanded:
                            contractions[expanded] = contracted
                        contracted, expanded = None, None
        return contractions

    def _add_contracted_forms(self, sentence):
        # handle two-token contractions
        for token1, token2 in lxcommon.utils.pairwise(sentence):
            if not token1.form.endswith("_"):
                continue
            expanded = (
                token1.form[:-1].lower().lstrip("-")
                + " "
                + token2.form.lower().lstrip("-")
            )
            contracted = self.contractions.get(expanded, None)
            if contracted:
                token1.raw = lxcommon.utils.recase_as(contracted, token1.form)
                token2.raw = None  # remove raw form of "virtual" token

    @staticmethod
    def _fix_spaces_around_quotes(sentence):
        if len(sentence) < 2:
            return
        for previous_token, current_token in lxcommon.utils.pairwise(sentence):
            if previous_token.form in LxTokenizer.OPEN_QUOTES:
                previous_token.add_space("L")
                previous_token.remove_space("R")
                current_token.remove_space("L")
            if current_token.form in LxTokenizer.CLOSE_QUOTES:
                previous_token.remove_space("R")
                current_token.remove_space("L")
                current_token.add_space("R")

    @staticmethod
    def _fix_spaces(sentence):
        if not sentence:
            return
        sentence[0].add_space("L")  # space at left of first token
        sentence[-1].add_space("R")  # space at right of last token
        if len(sentence) < 2:
            return
        # ensure that spacing information is consistent between neighbours
        # by keeping spaces only where both tokens agree;
        # also removes spaces between contracted tokens (where the left token
        # ends with _)
        for token1, token2 in lxcommon.utils.pairwise(sentence):
            if (
                "R" not in token1.space
                or "L" not in token2.space
                or token1.form.endswith("_")
            ):
                token1.remove_space("R")
                token2.remove_space("L")

    def tokenize_paragraph(self, paragraph):
        if isinstance(paragraph, str):
            lxparagraph = LxParagraph.from_cintil(
                paragraph, CintilFormatSpec(tokenized=False)
            )
        elif isinstance(paragraph, LxParagraph):
            # this test must come before
            # isinstance(paragraph, (list, tuple))
            # because LxParagraph is a subclass of list
            lxparagraph = paragraph
        elif isinstance(paragraph, (list, tuple)):
            lxparagraph = LxParagraph.from_primitive_types(paragraph)
        else:
            raise TypeError(
                "paragraph must be an instance of str, list/tuple (of dicts), "
                "or lxcommon.LxParagraph"
            )
        for lxsentence in lxparagraph:
            self.tokenize_sentence(lxsentence)
        lxparagraph.default_cintil_format_spec = LxTokenizer.CINTIL_FORMAT_SPEC
        return lxparagraph

    def tokenize_sentence(self, sentence):
        if isinstance(sentence, str):
            lxsentence = LxSentence.from_cintil(
                sentence, CintilFormatSpec(tokenized=False)
            )
        elif isinstance(sentence, LxSentence):
            lxsentence = sentence
        else:
            raise TypeError(
                "sentence must be an instance of str or lxcommon.LxSentence"
            )
        return self.tokenize_raw_sentence(lxsentence)

    def tokenize_raw_sentence(self, sentence):
        if isinstance(sentence, str):
            lxsentence = LxSentence(raw=sentence)
        elif isinstance(sentence, LxSentence):
            lxsentence = sentence
        else:
            raise TypeError(
                "sentence must be an instance of str or lxcommon.LxSentence"
            )
        if re.search("</?[sp]>", lxsentence.raw, re.IGNORECASE):
            raise ValueError("unexpected <s>, <p>, </s> or </p> tags in sentence.raw")
        # discard any characters that cannot be represented in ISO-8859-1:
        raw_sentence = lxcommon.utils.normalize_text(lxsentence.raw)
        tokenizer_input = f"<s> {raw_sentence} </s>"
        self.writeline(tokenizer_input)
        tokenizer_output = self.readline().strip()
        # under some conditions, the tokenizer delays outputing </s> until a new
        # sentence is fed; in such situations, we skip the </s> and get the next line:
        if tokenizer_output == "</s>":  
            tokenizer_output = self.readline().strip()
        ok = True
        if not tokenizer_output.startswith("<s>"):
            ok = False
            LOG.warning("tokenizer removed <s> from begining of line")
        if not tokenizer_output.endswith("</s>"):
            ok = False
            LOG.warning("tokenizer removed </s> from end of line")
        if not ok:
            LOG.warning(f"tokenizer input: {tokenizer_input!r}")
            LOG.warning(f"tokenizer output: {tokenizer_output!r}")
        tokenizer_output = tokenizer_output.replace("<s>", "").replace("</s>", "")
        forms = tokenizer_output.strip().split()
        forms = [
            clean_form for unclean_form in forms
            for clean_form in LxTokenizer._separate_quotes(unclean_form)
        ]
        forms = [
            clean_form for unclean_form in forms
            for clean_form in LxTokenizer._separate_slashes(unclean_form)
        ]
        tokens = LxTokenizer._create_tokens(forms)
        LxTokenizer._fix_spaces_around_quotes(tokens)
        self._add_contracted_forms(tokens)
        LxTokenizer._fix_spaces(tokens)
        lxsentence[:] = tokens
        lxsentence.default_cintil_format_spec = LxTokenizer.CINTIL_FORMAT_SPEC
        return lxsentence


__all__ = ["LxTokenizer"]
