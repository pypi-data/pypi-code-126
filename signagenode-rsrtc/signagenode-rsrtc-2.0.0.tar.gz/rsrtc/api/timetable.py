

from twisted.internet.task import LoopingCall
from twisted.internet import reactor
from .core import RsrtcApiCoreEngine


class RsrtcTimetableEngine(RsrtcApiCoreEngine):
    _api_ep_timetable = 'bus-schedules'

    def __init__(self, *args, **kwargs):
        super(RsrtcTimetableEngine, self).__init__(*args, **kwargs)
        self._retries = 0
        self._rapid_checks = 0
        self._api_timetable_task = None

    def _api_timetable_handler(self, response):
        self.log.info("Got Timetable API Response with {n} Entries",
                      n=len(response))
        if len(response):
            self._retries = 0
            self._rapid_checks = 0
            self._actual.rsrtc_timetable_update(response)
        else:
            self._retries += 1
            if self._retries >= 3:
                self._rapid_checks += 1
                if self._rapid_checks < 10:
                    reactor.callLater(60, self.api_get_timetable)
                self._actual.rsrtc_timetable_update(response)
            else:
                self.api_get_timetable()

    def _api_timetable_params(self, token):
        rv = self._api_basic_params(token)
        rv['_query'].append(('code', self.config.rsrtc_stop_id))
        return rv

    def api_get_timetable(self):
        return self._api_execute(
            self._api_ep_timetable,
            self._api_timetable_params,
            self._api_timetable_handler
        )

    """ Timetable API Management Task """
    @property
    def api_timetable_task(self):
        if self._api_timetable_task is None:
            self._api_timetable_task = LoopingCall(self.api_get_timetable)
        return self._api_timetable_task
