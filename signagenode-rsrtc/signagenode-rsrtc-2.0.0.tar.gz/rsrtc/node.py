

import os
import pkg_resources

from kivy_garden.ebs.core.colors import GuiPalette
from ebs.linuxnode.core.config import ElementSpec, ItemSpec

from starxmedia.node import StarXMediaNode

from .timetable.rsrtc import RsrtcTimetableMixin

from .api import RsrtcApiEngine
from .api import SXMApiEngineRSRTC


class RsrtcNode(RsrtcTimetableMixin, StarXMediaNode):
    _palette = GuiPalette(
        background=(0xf7 / 255, 0xf7 / 255, 0xf7 / 255),
        foreground=(0xff / 255, 0xff / 255, 0xff / 255),
        color_1=(0x72 / 255., 0xc2 / 255., 0xf5 / 255., 1),
        color_2=(0x07 / 255., 0x3e / 255., 0xbc / 255., 1)
    )
    _gui_marquee_bgcolor = (0xff / 255., 0x00 / 255., 0x00 / 255., 0.6)
    _gui_supports_overlay_mode = True

    _appname = "rsrtc"
    _supported_languages = ['en_IN', 'hi_IN']
    _default_rsrtc_api_url = 'http://rsrtc.starxmedia.in:9091'

    def __init__(self, *args, **kwargs):
        super(RsrtcNode, self).__init__(*args, **kwargs)

    @property
    def rsrtc_version(self):
        return pkg_resources.get_distribution('infopanel-rsrtc').version

    def install(self):
        self.config.register_application_root(
            os.path.abspath(os.path.dirname(__file__))
        )

        sxm_api_engine = SXMApiEngineRSRTC(self)
        self.modapi_install(sxm_api_engine)

        super(RsrtcNode, self).install()

        _elements = {
            'rsrtc_api_url': ElementSpec('rsrtc', 'url', ItemSpec(str, fallback=self._default_rsrtc_api_url)),
            'rsrtc_stop_id': ElementSpec('rsrtc', 'stop_id', ItemSpec(str, fallback='JPR', read_only=False)),
            'rsrtc_stop_name': ElementSpec('rsrtc', 'stop_name', ItemSpec(str, fallback="", read_only=False)),
            'rsrtc_window_prior': ElementSpec('rsrtc', 'window_prior', ItemSpec(int, fallback=30, read_only=False)),
            'rsrtc_window_post': ElementSpec('rsrtc', 'window_post', ItemSpec(int, fallback=60, read_only=False)),
        }

        for name, spec in _elements.items():
            self.config.register_element(name, spec)

        rsrtc_api_engine = self.modapi_engine('rsrtc')
        if not rsrtc_api_engine:
            self.log.info("Installing Vanilla RSRTC Api Engine")
            rsrtc_api_engine = RsrtcApiEngine(self)
            self.modapi_install(rsrtc_api_engine)

        sxm_api_engine.install_task('api_rsrtc_settings_task', 3600)
        rsrtc_api_engine.install_task('api_timetable_task', 300)

    def start(self):
        super(RsrtcNode, self).start()

    def stop(self):
        super(RsrtcNode, self).stop()
