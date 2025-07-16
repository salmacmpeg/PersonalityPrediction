from components.model_all import build_model
from configs import model_settings_obj
from pathlib import Path
import pickle as pk


class model_loader_service():
    def __init__(self) -> None:
        self.model = None

    def load_model(self):
        """check if model exists, load it
        #if not, build it , save it, then load it
        #finally set the self.model with it"""
        model_path = Path(f'{model_settings_obj.MODELS_FOLDER}/' +
                          f'{model_settings_obj.MODEL_NAME}')

        if not model_path.exists():
            print("model was not found, so we build it again")
            build_model()

        with open(model_path, 'rb') as model_file:
            self.model = pk.load(model_file)
            print("Loaded model successfully")
