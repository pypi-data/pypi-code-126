import re
from regexes.quote import DOUBLE_QUOTE_REGEX, SINGLE_QUOTE_REGEX
from regexes.persian import PERSIAN_REGEX
from hazm import POSTagger, sent_tokenize, word_tokenize
from parsivar import Normalizer
import dictionary
from normalizer_utils import clean_url, extra_clean_txt, endings, fix_spaces, site_names
from emoji_remover import de_emojify
import string