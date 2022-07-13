from typing import List

from g2p_en import G2p

from ..constants import (
    G2P_PHONEMES_TO_SAY_PHONEMES
)


g2p = G2p()

def text_to_g2p_phonemes(text: str) -> List[str]:
    return g2p(text)

def text_to_say_phonemes(text: str) -> List[str]:
    g2p_phonemes = text_to_g2p_phonemes(text)
    return [G2P_PHONEMES_TO_SAY_PHONEMES.get(p, '') for p in g2p_phonemes]
