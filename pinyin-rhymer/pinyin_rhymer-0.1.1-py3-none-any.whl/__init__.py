__version__ = '0.1.0'

from pinyin_rhymer.pinyin import PinYin


def rhyme_with(source, consonants, vowels, tones):
    pinyin = PinYin(source)
    return pinyin.generate_rhymes(consonants, vowels, tones)
