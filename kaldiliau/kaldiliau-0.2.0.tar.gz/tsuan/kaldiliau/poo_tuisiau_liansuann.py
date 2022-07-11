import logging

from tuitse._kiamtsa import kiamtsa
from tuitse.boolean import tuitse_boolean
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器

from kaldiliau.kesi import kaSikan
from kaldiliau.poo_lomaji_liansuann import poo_lian


logger = logging.getLogger(__name__)

_mtsai = '{0}｜{0}'.format('UNK')


def pooLomaji_kah_sooji(wavPath, taibun):
    su = taibun.split()
    ko = []
    for tsua in poo_lian(wavPath, su, tsuanTuitsiau=True):
        *_tshun, khaisi, tngte, hunsu = tsua.split()
        if hunsu == '<unk>':
            hunsu = _mtsai
        kiatsok = kaSikan(khaisi, tngte)
        ko.append({
            'hunsu': hunsu,
            'khaisi': khaisi,
            'kiatsok': kiatsok,
            'tngte': tngte,
        })
    punte, kiangi = _khuann_kiangi(ko, su)
    for su, punte, kiangi in zip(ko, punte, kiangi):
        *_tshun, khaisi, tngte, hunsu = tsua.split()
        kiatsok = kaSikan(khaisi, tngte)
        su.update({
            'punte': punte,
            'kiangi': kiangi,
        })
        if su['hunsu'] == _mtsai:
            su['hunsu'] = '{0}｜{0}'.format(punte)
    return ko


def _khuann_kiangi(ko, punte_su):
    # Kiàn-li̍p DP pió
    dp_tin = [[], ]
    loo_tin = [[], ]
    for _ in range(len(punte_su) + 1):
        dp_tin[0].append((0, 0, 0))
        loo_tin[0].append('tah-té')
    for su in ko:
        tsua_dp = [(0, 0, 0), ]
        tsua_loo = ['tah-té', ]

        hanji = 拆文分析器.分詞詞物件(su['hunsu']).看語句()
        for binting, tshu, punte in zip(
            dp_tin[-1][1:], dp_tin[-1], punte_su
        ):
            kam_u = tuitse_boolean(kiamtsa(
                hanji, punte
            ))
            if punte.isnumeric():
                sooji_binting = (binting[0], binting[1] + 1, binting[2])
                sooji_tshu = (tshu[0], tshu[1] + 1, tshu[2])
                if sooji_tshu >= sooji_binting:
                    tsua_dp.append(sooji_tshu)
                    tsua_loo.append('sooji_tshu')
                else:
                    tsua_dp.append(sooji_binting)
                    tsua_loo.append('sooji_binting')
            elif kam_u:
                hah_tshu = (tshu[0] + 1, tshu[1], tshu[2])
                tsua_dp.append(hah_tshu)
                tsua_loo.append('tshu')
            else:
                # Bô tsit jī
                behah_tshu = (tshu[0], tshu[1], tshu[2] + 1)
                tsua_dp.append(behah_tshu)
                tsua_loo.append('behah_tshu')
        dp_tin.append(tsua_dp)
        loo_tin.append(tsua_loo)
    # Se̍h-thâu khuànn siáng ū tuì--tio̍h
    kiat_ko = []
    sin_punte = []
    tit = len(ko)
    huinn = len(punte_su)
    while tit > 0 and huinn > 0:
        hanji = 拆文分析器.分詞詞物件(ko[tit - 1]['hunsu']).看語句()
        punte = punte_su[huinn - 1]
        if loo_tin[tit][huinn] == 'tshu':
            tit -= 1
            huinn -= 1
            kiat_ko.append(punte)
            sin_punte.append(punte)
        elif loo_tin[tit][huinn] == 'sooji_binting':
            tit -= 1
            kiat_ko.append(hanji)
            sin_punte.append(punte)
        elif loo_tin[tit][huinn] == 'sooji_tshu':
            tit -= 1
            huinn -= 1
            kiat_ko.append(hanji)
            sin_punte.append(punte)
        elif loo_tin[tit][huinn] == 'behah_tshu':
            tit -= 1
            huinn -= 1
            kiat_ko.append(punte)
            sin_punte.append(punte)
    sin_punte.reverse()
    kiat_ko.reverse()
    return sin_punte, kiat_ko
