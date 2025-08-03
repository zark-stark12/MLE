import pickle
from pathlib import Path
from model import build_model
from config import settings
from loguru import logger   

def load_model(path=''):
    pass

class ModelService:

    def __init__(self):
        self.model = None

    def load_model(self):
        logger.info(f"Checking model exisgs")
        model_path = Path(f'{settings.model_path}/{settings.model_name}')

        if not model_path.exists():
            logger.info("Did not find existing model. Building new model")
            build_model(settings.model_name)
        logger.info(f"Loading pickled model at {settings.model_path}/{settings.model_name}")
        self.model = pickle.load(open(f'{settings.model_path}/{settings.model_name}', 'rb'))

    def predict(self, input_parameters):
        logger.info(f"Predicting model with given inputs: {input_parameters}")
        return self.model.predict([input_parameters])
    