

from twisted.internet.task import LoopingCall
from starxmedia.api.core import SXMApiEngineCore


class SXMApiExtentionRSRTC(SXMApiEngineCore):
    _api_ep_device_rsrtc_settings = 'iot/load-device-rsrtc-details'

    def __init__(self, *args, **kwargs):
        super(SXMApiExtentionRSRTC, self).__init__(*args, **kwargs)
        self._api_rsrtc_settings_task = None

    def _api_apply_device_rsrtc_settings(self, settings):
        self.log.info("Got device rsrtc settings from the server : {settings}",
                      settings=settings)
        self.config.rsrtc_stop_id = settings['stop_code']
        self.config.rsrtc_stop_name = settings['stop_name']
        if 'window_prior' in settings.keys():
            self.config.rsrtc_window_prior = settings['window_prior']
        if 'window_post' in settings.keys():
            self.config.rsrtc_window_post = settings['window_post']

    def _api_device_rsrtc_settings_handler(self, response):
        self._api_apply_device_rsrtc_settings(response['data'])

    def api_get_device_rsrtc_settings(self):
        return self._api_execute(
            self._api_ep_device_rsrtc_settings,
            self._api_basic_params,
            self._api_device_rsrtc_settings_handler
        )

    @property
    def api_rsrtc_settings_task(self):
        if self._api_rsrtc_settings_task is None:
            self._api_rsrtc_settings_task = LoopingCall(self.api_get_device_rsrtc_settings)
        return self._api_rsrtc_settings_task
