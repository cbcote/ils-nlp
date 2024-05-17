# scripts/evaluate_model.py
import argparse
import pandas as pd
from src.utils.config_loader import ConfigLoader
from src.models.text_classification import TextClassificationModel
from src.models.model_utils import evaluate_model

def main():
    parser = argparse.ArgumentParser(description='Evaluate text classification model.')
    parser.add_argument('--data', required=True, help='Path to evaluation data CSV file')
    args = parser.parse_args()

    # Load configuration
    config = ConfigLoader.load_config('config/config.yaml')

    # Load evaluation data
    data = pd.read_csv(args.data)
    X = data['text']
    y = data['label']

    # Initialize and load the model
    model = TextClassificationModel(config['model']['model_path'])
    model.load_model()

    # Make predictions
    y_pred = model.predict(X)

    # Evaluate the model
    metrics = evaluate_model(y, y_pred)
    print(metrics)

if __name__ == '__main__':
    main()
