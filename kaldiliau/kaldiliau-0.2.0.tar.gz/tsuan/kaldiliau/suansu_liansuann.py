import json
import logging

from kaldiliau.kesi import post_liansuann, get_liansuann


logger = logging.getLogger(__name__)


def suansu(imtong, suanhang):
    ko = []
    for tsua in _piansik_lian(
        'ji_fst_decoding_rescoring_nbest',
        imtong, suanhang
    ):
        *_tshun, hunsu, _SIL = tsua.split()
        ko.append({
            'hunsu': hunsu,
        })
    return ko


def _piansik_lian(piansik, wavPath, suanhang):
    tshamsoo = {'wav': wavPath}
    with post_liansuann('ling_kaldi_format', tshamsoo) as inue:
        tmpPath = json.loads(inue)
        logger.debug('ling %s', tmpPath)
    with post_liansuann('it_suansu', {
        'tmpTonganSootsai': tmpPath,
        'suanhang': json.dumps(suanhang),
    }) as inue:
        logger.debug('ling %s', json.loads(inue))
    with post_liansuann(piansik, {'tmpTonganSootsai': tmpPath}) as inue:
        logger.debug('ji %s',  json.loads(inue))
    with get_liansuann('sam_nbest', tmpPath) as inue:
        nbest = json.loads(inue)
        logger.debug('sam \n%s', ''.join(nbest))
    return nbest
