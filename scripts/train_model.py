import argparse
import pandas as pd
from src.utils.config_loader import ConfigLoader
from src.models.text_classification import TextClassificationModel

def main():
    parser = argparse.ArgumentParser(description='Train text classification model.')
    parser.add_argument('--data', required=True, help='Path to training data CSV file')
    args = parser.parse_args()

    # Load configuration
    config = ConfigLoader.load_config('config/config.yaml')

    # Load training data
    data = pd.read_csv(args.data)
    X = data['text']
    y = data['label']

    # Initialize and train the model
    model = TextClassificationModel(config['model']['model_path'])
    model.train(X, y)

if __name__ == '__main__':
    main()
