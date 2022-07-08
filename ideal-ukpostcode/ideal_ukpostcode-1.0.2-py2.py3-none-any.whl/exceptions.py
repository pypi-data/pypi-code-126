class InvalidArea(Exception):
    def __init__(self, msg='Invalid postcode area'):
        super().__init__(msg)


class InvalidDistrict(Exception):
    def __init__(self, msg='Invalid postcode district'):
        super().__init__(msg)


class InvalidSector(Exception):
    def __init__(self, msg='Invalid postcode sector'):
        super().__init__(msg)


class InvalidUnit(Exception):
    def __init__(self, msg='Invalid postcode unit'):
        super().__init__(msg)
