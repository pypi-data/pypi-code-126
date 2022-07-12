import itertools
import re

from pinyin_rhymer.consonant import Consonant
from pinyin_rhymer.data.pinyin_list import PINYIN_LIST
from pinyin_rhymer.error import NotAPinYinError
from pinyin_rhymer.rhyme_scheme import ConsonantScheme, VowelScheme
from pinyin_rhymer.vowel import Vowel

TONES = 'āēīōūǖáéíóúǘǎěǐǒǔǚàèìòùǜ'
REPLACE = 'aāáǎàeēéěèiīíǐìoōóǒòuūúǔùvǖǘǚǜ'
ZCS = 'zcs'
ZHCHSHR = ('zh', 'ch', 'sh', 'r')
BPMF = 'bpmf'
JQX = 'jqx'
RE_PINYIN = re.compile(
    fr'^([{"".join(Consonant.all_as_str())}]*)([eaiouvngwy]+)(\d)?$'
)


def convert_unicode_to_alnum(pinyin):
    """
    Convert an unicode string of pinyin into an alphanumeric one.
    """
    for c in pinyin:
        if c in TONES:
            i = TONES.find(c)
            vowel = i % 6
            tone = i // 6 + 1
            pinyin = f'{pinyin.replace(c, REPLACE[vowel*5])}{tone}'
            break
    return pinyin


def transform_vowel(consonant, vowel):
    match vowel:
        case 'i':
            if consonant in ZCS:
                return 'z'
            if consonant in ZHCHSHR:
                return 'r'
        case 'o':
            if consonant in BPMF:
                return 'uo'
    if consonant and consonant in JQX:
        return vowel.replace('u', 'v')
    return vowel


def reverse_transform_vowel(consonant, vowel):
    match vowel:
        case 'uo':
            if consonant in BPMF:
                return 'o'
    if consonant and consonant in JQX:
        return vowel.replace('v', 'u')
    return vowel


class PinYin(object):
    def __init__(self, in_str, vowel=None, tone=1):
        consonant = in_str
        if not vowel:
            consonant, vowel, tone = self._parse(in_str)
        self.consonant = Consonant.get(consonant)
        self.vowel = Vowel(vowel)
        self.tone = int(tone)

    def _parse(self, pinyin):
        if not pinyin.isascii():
            pinyin = convert_unicode_to_alnum(pinyin)
        groups = RE_PINYIN.match(pinyin)
        if not groups:
            raise NotAPinYinError(pinyin)

        consonant = groups.group(1)
        vowel = groups.group(2)
        vowel = transform_vowel(consonant, vowel)
        tone = groups.group(3) or 5

        return consonant, vowel, tone

    @property
    def spell_vowel(self):
        consonant = str(self.consonant)
        vowel = (
            self.vowel.with_consonant if consonant
            else self.vowel.without_consonant
        )
        return reverse_transform_vowel(consonant, vowel)

    @property
    def is_valid(self):
        return str(self) in PINYIN_LIST

    def __str__(self):
        return f'{self.consonant}{self.spell_vowel}{self.tone}'

    def __hash__(self):
        return hash(self.with_tone_mark())

    def __eq__(self, other):
        return str(self) == other or hash(self) == hash(other)

    def with_tone_mark(self):
        vowel = self.spell_vowel
        if len(vowel) == 1:
            replace = vowel
        elif 'a' in vowel:
            replace = 'a'
        elif 'e' in vowel:
            replace = 'e'
        elif 'o' in vowel:
            replace = 'o'
        elif 'n' in vowel:
            replace = self.vowel.nucleus
        else:
            replace = vowel[1]
        vowel = vowel.replace(
            replace, REPLACE[REPLACE.index(replace) + (self.tone % 5)]
        )
        return f'{self.consonant}{vowel}'

    def generate_rhymes(self, consonants, vowels, tones):
        consonants = self._get_consonant_list(consonants)
        vowels = self._get_vowel_list(vowels)
        tones = self._get_tone_list(tones)
        for consonant in consonants:
            for vowel in vowels:
                for tone in tones:
                    pinyin = PinYin(consonant, vowel, tone)
                    if pinyin.is_valid:
                        yield pinyin

    def _get_consonant_list(self, consonants):
        try:
            consonants = ConsonantScheme(consonants)
        except ValueError:
            # 'bpmf'
            return (Consonant.get(x) for x in consonants)
        except TypeError:
            # ('b', 'p', 'm', 'f') or ('FAMILY', 'b', 'p', 'm', 'f')
            return itertools.chain.from_iterable(
                self._get_consonant_list(x) for x in consonants
            )
        else:
            match consonants:
                case ConsonantScheme.ALL:
                    return Consonant.all_as_str()
                case ConsonantScheme.FAMILY:
                    return self.consonant.family()

    def _get_vowel_list(self, vowels):
        try:
            vowels = VowelScheme(vowels)
        except ValueError:
            return (Vowel(x) for x in re.split(r'[\s\t,]+', vowels))
        except TypeError:
            return itertools.chain.from_iterable(
                self._get_vowel_list(x) for x in vowels
            )
        else:
            match vowels:
                case VowelScheme.TRADITIONAL:
                    return self.vowel.similar_traditional()
                case VowelScheme.SIMILAR_SOUNDING:
                    return self.vowel.similar_sounding()
                case VowelScheme.ADDTIIVE:
                    return self.vowel.similar_additive()
                case VowelScheme.SUBTRACTIVE:
                    return self.vowel.similar_subtractive()

    def _get_tone_list(self, tones):
        if tones == 'ALL':
            return range(1, 6)
        return tones
