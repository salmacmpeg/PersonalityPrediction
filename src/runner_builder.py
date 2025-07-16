from pipeline.model_load_pipeline import model_loader_service
from loguru import logger


@logger.catch
def main():
    mls = model_loader_service()
    mls.load_model()


if __name__ == '__main__':
    main()
