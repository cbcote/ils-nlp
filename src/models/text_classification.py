import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from src.models.base import BaseModel

class TextClassificationModel(BaseModel):
    def __init__(self, model_path):
        super().__init__(model_path)
        self.vectorizer = TfidfVectorizer()
        self.model = LogisticRegression()

    def train(self, X, y):
        """
        Train the model on the given data.
        
        Args:
            X: List of input data
            y: List of target labels
        
        Returns:
            None
        """
        X_transformed = self.vectorizer.fit_transform(X)
        self.model.fit(X_transformed, y)
        self.save_model()

    def predict(self, X):
        """
        Make predictions on the given data.
        
        Args:
            X: List of input data
        
        Returns:
            List of predicted labels
        """
        if self.model is None:
            self.load_model()
        X_transformed = self.vectorizer.transform(X)
        return self.model.predict(X_transformed)

    def save_model(self):
        """
        Save the model to disk.
        
        Returns:
            None
        """
        super().save_model()
        joblib.dump(self.vectorizer, self.model_path + '_vectorizer')
        print(f"Vectorizer saved to {self.model_path}_vectorizer")

    def load_model(self):
        """
        Load the model from disk.
        
        Returns:
            None
        """
        super().load_model()
        self.vectorizer = joblib.load(self.model_path + '_vectorizer')
        print(f"Vectorizer loaded from {self.model_path}_vectorizer")
