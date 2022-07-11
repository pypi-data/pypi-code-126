import json
import logging

from kaldiliau.kesi import post_liansuann, get_liansuann, kaSikan


logger = logging.getLogger(__name__)


def tuitse(imtong, taibun_tsua):
    kaldi結果 = pooLomaji(imtong, ' '.join(taibun_tsua))
    ko = []
    tsitma = 0
    for tsua in taibun_tsua:
        liong = len(tsua.split())
        su = kaldi結果[tsitma:tsitma + liong]
        kukhaisi = su[0]['khaisi']
        kukiatsok = su[-1]['kiatsok']
        kutngte = '0.00'
        for s in su:
            kutngte = kaSikan(kutngte, s['tngte'])
        ko.append({
            'su': su,
            'khaisi': kukhaisi,
            'kiatsok': kukiatsok,
            'tngte': kutngte,
        })
        tsitma += liong
    return ko


def pooLomaji(wavPath, taibun):
    su = taibun.split()
    ko = []
    for tsua, punte in zip(poo_lian(wavPath, su, tsuanTuitsiau=False), su):
        *_tshun, khaisi, tngte, hunsu = tsua.split()
        if hunsu == '<unk>':
            hunsu = '{0}｜{0}'.format(punte)
        kiatsok = kaSikan(khaisi, tngte)
        ko.append({
            'punte': punte,
            'hunsu': hunsu,
            'khaisi': khaisi,
            'kiatsok': kiatsok,
            'tngte': tngte,
        })
    return ko


def poo_lian(wavPath, taiBun, tsuanTuitsiau):
    ling_tshamsoo = {'wav': wavPath, }
    with post_liansuann('ling_kaldi_format', ling_tshamsoo) as inue:
        tmpPath = json.loads(inue)
        logger.debug('ling %s', tmpPath)
    it_tshamsoo = {
        'tmpTonganSootsai': tmpPath,
        'taibun': json.dumps(taiBun),
        'tsuanTuitsiau': tsuanTuitsiau,
    }
    with post_liansuann('it_poolmj', it_tshamsoo) as inue:
        logger.debug('it %s', json.loads(inue))
    with post_liansuann('ji_fst_decoding_koh_rescoring', {
        'tmpTonganSootsai': tmpPath
    }) as inue:
        logger.debug('ji %s', json.loads(inue))
    with get_liansuann('sam_sikan', tmpPath) as inue:
        sikan = json.loads(inue)
        logger.debug('sam \n%s', ''.join(sikan))
    return sikan
