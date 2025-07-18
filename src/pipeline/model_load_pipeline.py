from src.components.model_all import build_model
from src.configs import model_settings_obj
from pathlib import Path
import pickle as pk
from loguru import logger


class model_loader_service():
    def __init__(self) -> None:
        self.model = None
        self.highest_score = -1

    def load_model(self):
        """check if model exists, load it
        #if not, build it , save it, then load it
        #finally set the self.model with it"""
        model_path = Path(f'{model_settings_obj.MODELS_FOLDER}/' +
                          f'{model_settings_obj.MODEL_NAME}')

        if not model_path.exists():
            logger.warning("model was not found, so we build it again")
            build_model()

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)
            logger.info("Loaded model successfully in model loader")

    def load_highest_score(self):
        file_path = f'{model_settings_obj.MODELS_FOLDER}/' \
                 f'{model_settings_obj.HIGH_SCORE_FILE_NAME}'
        if Path(file_path).exists():
            with open(file_path, 'r') as file:
                self.highest_score = float(file.readline())
                logger.debug(f'Loaded highest score of : {self.highest_score}')
        else:
            logger.warning(f'highest score File {file_path} does not exist')
