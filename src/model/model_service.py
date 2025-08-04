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
from config.config import settings

class ModelService:
    """
    A service class for manaing 
    """
    def __init__(self):
        self.model = None

    def load_model(self):
        logger.info(f"Checking model exists")
        model_path = Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            logger.warning("Did not find existing model. Building new model")
            build_model()
        logger.info(f"Loading pickled model at {settings.model_path}/{settings.model_name}")
        self.model = pickle.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))

    def predict(self, input_parameters):
        logger.info(f"Predicting model with given inputs: {input_parameters}")
        return self.model.predict([input_parameters])
    