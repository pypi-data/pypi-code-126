import itertools
import re

from pinyin_rhymer.consonant import Consonant
from pinyin_rhymer.data.pinyin_list import PINYIN_LIST
from pinyin_rhymer.rhyme_scheme import ConsonantScheme, VowelScheme
from pinyin_rhymer.vowel import Vowel

TONES = 'āēīōūǖáéíóúǘǎěǐǒǔǚàèìòùǜ'
REPLACE = 'aāáǎàeēéěèiīíǐìoōóǒòuūúǔùvǖǘǚǜ'
ZCS = 'zcs'
ZHCHSHR = ('zh', 'ch', 'sh', 'r')
BPMF = 'bpmf'
JQX = 'jqx'
RE_PINYIN = re.compile(fr'^([{Consonant.all()}]*)([eaiouvngwy]+)(\d)?')


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
    def __init__(self, pinyin):
        if not pinyin.isascii():
            pinyin = convert_unicode_to_alnum(pinyin)
        groups = RE_PINYIN.match(pinyin)
        consonant = groups.group(1)
        vowel = groups.group(2)
        vowel = transform_vowel(consonant, vowel)
        self.consonant = Consonant.get(consonant)
        self.vowel = Vowel(vowel)
        self.tone = int(groups.group(3) or 5)

    def generate_rhymes(self, consonants, vowels, tones):
        consonants = self._get_consonant_list(consonants)
        vowels = self._get_vowel_list(vowels)
        tones = self._get_tone_list(tones)
        pinyin_list = PINYIN_LIST.get_pinyin()
        for consonant in consonants:
            for vowel in vowels:
                for tone in tones:
                    vowel = (
                        vowel.with_consonant if consonant
                        else vowel.without_consonant
                    )
                    vowel = reverse_transform_vowel(consonant, vowel)
                    pinyin = f'{consonant}{vowel}{tone}'
                    if pinyin in pinyin_list:
                        yield pinyin

    def _get_consonant_list(self, consonants):
        try:
            consonants = ConsonantScheme(consonants)
        except ValueError:
            # 'bpmf'
            return (
                Consonant.get(
                    x.replace('Z', 'zh').replace('C', 'ch').replace('S', 'sh')
                ) for x in consonants
            )
        except TypeError:
            # ('b', 'p', 'm', 'f') or ('FAMILY', 'b', 'p', 'm', 'f')
            return itertools.chain.from_iterable(
                self._get_consonant_list(x) for x in consonants
            )
        else:
            match consonants:
                case ConsonantScheme.ALL:
                    return Consonant.all()
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
