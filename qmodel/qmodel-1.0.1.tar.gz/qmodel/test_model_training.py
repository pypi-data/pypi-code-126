import unittest
from .model_training import ModelTraining


class TestModelTraining(unittest.TestCase):

    def test_existence(self):
        og_10_img_path = "path of the training set"
        model_training = ModelTraining(og_10_img_path , "path where to save the model"  )
        model_training.train()
        model_path = model_training.get_model_path()

        self.assertEqual(model_path ,"full path of the rfc model with extension (.joblib)" )



if __name__ == "__main__":
    unittest.main()