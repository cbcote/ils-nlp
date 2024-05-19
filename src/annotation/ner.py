import spacy
from spacy.training import Example
from spacy.tokens import DocBin
import logging

class NERModel:
    def __init__(self, model_name='en_core_web_sm', custom_model_path=None):
        """
        Initialize the NER model.
        
        Args:
            model_name: Name of the pre-trained SpaCy model to use.
            custom_model_path: Path to a custom-trained model, if available.
        """
        # Initialize logger to track model loading, training, and saving
        self.logger = logging.getLogger(__name__)
        
        # Load the custom model if available, otherwise load the pre-trained model
        if custom_model_path:
            self.nlp = spacy.load(custom_model_path)
            self.logger.info(f"Loaded custom model from {custom_model_path}")
        else:
            self.nlp = spacy.load(model_name)
            self.logger.info(f"Loaded pre-trained model: {model_name}")

    def extract_entities(self, text: str) -> list[tuple[int, int, str]]:
        """
        Extract named entities from the text.
        
        Args:
            text: Text to analyze.
        
        Returns:
            List of entities with start and end positions and entity labels.
        """
        # Process the text with the NER model
        doc = self.nlp(text)
        # Extract entities from the processed text
        return [(ent.start_char, ent.end_char, ent.label_) for ent in doc.ents]

    def train_custom_model(self, training_data, output_dir, n_iter=100):
        """
        Train a custom NER model.
        
        Args:
            training_data: List of tuples in the format (text, {"entities": [(start, end, label)]}).
            output_dir: Directory to save the trained model.
            n_iter: Number of training iterations.
        """
        nlp = spacy.blank("en")  # Create a blank Language class
        
        # Add NER component to the pipeline
        if "ner" not in nlp.pipe_names:
            ner = nlp.add_pipe("ner", last=True)
        else:
            # If NER component already exists, get it
            ner = nlp.get_pipe("ner")

        # Add labels to the NER component
        for _, annotations in training_data:
            for ent in annotations.get("entities"):
                ner.add_label(ent[2])

        # Initialize the model with training data
        optimizer = nlp.begin_training()
        
        # Convert training data to Example objects
        for i in range(n_iter):
            self.logger.info(f"Starting iteration {i}")
            losses = {}
            
            # Shuffle training data for each iteration
            for text, annotations in training_data:
                example = Example.from_dict(nlp.make_doc(text), annotations)
                nlp.update([example], drop=0.35, losses=losses)
            
            # Log the training loss at each iteration
            self.logger.info(f"Losses at iteration {i}: {losses}")

        # Save the model
        nlp.to_disk(output_dir)
        self.logger.info(f"Saved custom model to {output_dir}")

    def save_model(self, output_dir):
        """
        Save the current model to a directory.
        
        Args:
            output_dir: Directory to save the model.
        """
        # Save the model to the output directory
        self.nlp.to_disk(output_dir)
        self.logger.info(f"Model saved to {output_dir}")

    def load_model(self, model_path):
        """
        Load a model from a directory.
        
        Args:
            model_path: Path to the model directory.
        """
        # Load the model from the specified path
        self.nlp = spacy.load(model_path)
        self.logger.info(f"Model loaded from {model_path}")
