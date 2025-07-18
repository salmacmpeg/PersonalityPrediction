from src.configs import model_settings_obj
from pathlib import Path
import pandas as pd
import pickle as pk
from loguru import logger


class model_inference_service():
    def __init__(self) -> None:
        self.model = None
        self._classes = ['Extrovert', 'Introvert']
        """check if model exists, load it
        #if not, build it , save it, then load it
        #finally set the self.model with it"""
        model_path = Path(f'{model_settings_obj.MODELS_FOLDER}/' +
                          f'{model_settings_obj.MODEL_NAME}')

        if not model_path.exists():
            logger.warning("model was not found, "
                           "please build it and run again")
            raise FileNotFoundError("no built model was not found,"
                                    "  please build it and run again")

        else:
            with open(model_path, 'rb') as model_file:
                self.model = pk.load(model_file)
                logger.info("Loaded model successfully in model inference")

    def predict(self, features: pd.DataFrame) -> int:
        """check if model exists, predict """
        if self.model is not None:
            if isinstance(features, pd.DataFrame):
                return self.model.predict(features)
            else:
                raise ValueError("features must be a pandas DataFrame")
        else:
            logger.warning("model was not found, "
                           "please build it and run again")
            raise FileNotFoundError("no built model was not found,"
                                    "  please build it and run again")
