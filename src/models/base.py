from abc import ABC, abstractmethod
import joblib
import os

class BaseModel(ABC):
    def __init__(self, model_path: str):
        self.model_path = model_path
        self.model = None

    @abstractmethod
    def train(self, X, y):
        """
        Train the model on the given data.
        
        Args:
            X: List of input data
            y: List of target labels
        
        Returns:
            None
        """
        pass

    @abstractmethod
    def predict(self, X):
        """
        Make predictions on the given data.
        
        Args:
            X: List of input data
        
        Returns:
            List of predicted labels
        """
        pass

    def save_model(self):
        """Save the model to disk."""
        os.makedirs(os.path.dirname(self.model_path), exist_ok=True)
        joblib.dump(self.model, self.model_path)
        print(f"Model saved to {self.model_path}")

    def load_model(self):
        """Load the model from disk."""
        if os.path.exists(self.model_path):
            self.model = joblib.load(self.model_path)
            print(f"Model loaded from {self.model_path}")
        else:
            raise FileNotFoundError(f"No model found at {self.model_path}")
