import unittest
from .model_testing import ModelTesting

class TestModelTesting(unittest.TestCase):

    def test_existence(self):

        testing_set_path = "path of the testing set"
        model_path ="path of the RFC model"

        model_test = ModelTesting(testing_set_path, model_path)

        inverted_resulted , accuracy = model_test.prediction()

        print(accuracy)

        self.assertEqual(accuracy , 1)

if __name__ == "__main__":
    unittest.main()