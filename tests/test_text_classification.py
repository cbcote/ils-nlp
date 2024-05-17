import unittest
from src.models.text_classification import TextClassificationModel

class TestTextClassificationModel(unittest.TestCase):
    def setUp(self):
        self.model = TextClassificationModel('models/test_model.pkl')
        self.X_train = ["sample text data", "another sample text"]
        self.y_train = [0, 1]

    def test_train(self):
        self.model.train(self.X_train, self.y_train)
        self.assertIsNotNone(self.model.model)

    def test_predict(self):
        self.model.train(self.X_train, self.y_train)
        predictions = self.model.predict(["sample text data"])
        self.assertEqual(len(predictions), 1)

if __name__ == '__main__':
    unittest.main()
