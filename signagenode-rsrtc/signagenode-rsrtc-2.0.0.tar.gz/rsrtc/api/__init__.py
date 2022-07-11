

from .timetable import RsrtcTimetableEngine


class RsrtcApiEngine(RsrtcTimetableEngine):
    pass


from starxmedia.api import SXMApiEngine
from .sxmext import SXMApiExtentionRSRTC


class SXMApiEngineRSRTC(SXMApiExtentionRSRTC, SXMApiEngine):
    pass
