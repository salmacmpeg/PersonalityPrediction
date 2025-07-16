from configs import model_settings_obj
from pathlib import Path
import pickle as pk
from loguru import logger


class model_inference_service():
    def __init__(self) -> None:
        self.model = None

    def predict(self, features):
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
                logger.info("Loaded model successfully")
                return self.model.predict(features)
