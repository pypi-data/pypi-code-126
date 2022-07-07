import unittest, os
from enum import Enum
from facebookcloudapi.utils import clean_dict

class TestType(Enum):
    KEY = "key"
    VALUE = "value"


class TestUtils(unittest.TestCase):

    def test_clean_dict(self):
        data = {
            TestType.KEY: TestType.VALUE
        }
        for key, value in data.items():
            self.assertIsInstance(key, Enum)
            self.assertIsInstance(value, Enum)

        for key,value in clean_dict(data).items():
            self.assertNotIsInstance(key, Enum)
            self.assertNotIsInstance(value, Enum)


if __name__ == '__main__':
    unittest.main()
