"""
This module provides functionality for managing our ML regression model

It contains the ModelService class which handles loading, using, and if needing
training our ML model if no such model exists. It loads the model from a file or builds
the model which is used to make predictions
"""

import pickle
from pathlib import Path

from loguru import logger

from model.pipeline.model import build_model
from config import model_settings

class ModelService:
    """
    A service class for managing the ML model.

    This class provides functionalities to load a ML model from a pre-specified location, build it if it doesn't exist,
    and make predictions using the said ML model.

    Attributes:
        model: ML model managed by this service. Initialized as None.

    Methods:
        __init__: Constructor that initializes the ModelService
        load_model: loads the from file or builds it if it doesn't exist
        predict: Makes a prediction using the loaded model
    """
    def __init__(self):
        """Initializes the Model services with no model loaded"""
        self.model = None

    def load_model(self):
        """Loads the model from a specified path or builds it if it doesn't exist"""
        logger.info(f"Checking model exists")
        model_path = Path(f'{model_settings.model_path}/{model_settings.model_name}')

        if not model_path.exists():
            logger.warning("Did not find existing model. Building new model")
            build_model()
        logger.info(f"Loading pickled model at {model_settings.model_path}/{model_settings.model_name}")
        self.model = pickle.load(open(f'{model_settings.model_path}/{model_settings.model_name}', 'rb'))

    def predict(self, input_parameters):
        """
        Makes predictions using loaded model

        Takes input parameters and passes it to the model which was loaded
        using a pickle file.

        Args:
            input_parameters (list): The input data for making a prediction.

        Returns:
            list: The prediction results from the model
        """
        logger.info(f"Predicting model with given inputs: {input_parameters}")
        return self.model.predict([input_parameters])
    