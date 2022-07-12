from .zt_engines import ZTEngineFirst
from .zt_engines import ZTPlayerFirst


class PvC(ZTEngineFirst, ZTPlayerFirst):
    """Class for the PvC Game"""

    def __init__(self, _engine_first: bool = True) -> None:
        """Initialize the Game

        :param _engine_first: Specifies if the engine starts first
        :type _engine_first: bool
        :return: None
        """

        if _engine_first:
            self.parent = ZTEngineFirst
            ZTEngineFirst.__init__(self)

        else:
            self.parent = ZTPlayerFirst
            ZTPlayerFirst.__init__(self)

    def play(self, pos: int) -> None:
        self.parent.play(self, pos)
