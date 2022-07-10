class specialTensor:
    def __init__(self, pd):
        self.__parmdegree = pd

    @classmethod
    def default(cls):
        return cls(1)

    @property
    def parmDegree(self):
        return self.__parmdegree

    @parmDegree.setter
    def parmDegree(self, var):
        assert var >= 1, "Param Degree cannot be less then 1"
        assert type(var) == int, "Param degree has to be int"
        self.__parmdegree = var

#br2 = specialTensor(2)
