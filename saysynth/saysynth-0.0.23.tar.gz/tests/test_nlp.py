from saysynth.utils import here
from saysynth.lib import nlp
from saysynth.constants import SAY_ALL_PHONEMES, G2P_PHONEMES_TO_SAY_PHONEMES


def test_g2p_phonemes_to_say_phonemes():
    g2p_texts = nlp.text_to_g2p_phonemes('hello world')
    for t in g2p_texts:
        if t.strip():
            assert t in G2P_PHONEMES_TO_SAY_PHONEMES
    say_texts = nlp.text_to_say_phonemes('hello world')
    for t in say_texts:
        if t.strip():
            assert t in set(G2P_PHONEMES_TO_SAY_PHONEMES.values())