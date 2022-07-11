

import arrow
from twisted.internet import reactor
from twisted.internet.task import LoopingCall

from rsrtc import api
from ebs.iot.linuxnode.modapi.standalone import StandaloneActual
from ebs.iot.linuxnode.modapi.standalone import StandaloneConfig


stop_id = 'JPR'


class StandaloneActualRsrtc(StandaloneActual):
    def rsrtc_timetable_update(self, response):
        nitems = len(response)
        items = [x['routeNo'] for x in response]
        ditems = set(items)
        ndistinct = len(ditems)
        print("{} : {:>3} results : {:>3} distinct : {}".format(
            arrow.now(), nitems, ndistinct, ditems))


class StandaloneConfigRsrtc(StandaloneConfig):
    def __init__(self, *args, **kwargs):
        self.rsrtc_stop_id = kwargs.pop('stop_id', 'KTH')
        super(StandaloneConfigRsrtc, self).__init__(*args, **kwargs)
        self.rsrtc_api_url = 'http://180.92.168.54:8082/RsrtcThirdPartyService'


config = StandaloneConfigRsrtc(stop_id=stop_id)
e = api.RsrtcApiEngine(StandaloneActualRsrtc(), config=config)


def get_results_summary():
    e.api_get_timetable()


if __name__ == '__main__':
    period = 5.0
    print("API Response Summary Test:")
    print(" API Url : {}".format(config.rsrtc_api_url))
    print(" Stop Code: {}".format(config.rsrtc_stop_id))
    print(" Period: {}s".format(period))
    loop = LoopingCall(get_results_summary)
    loopDeferred = loop.start(period)
    reactor.run()
