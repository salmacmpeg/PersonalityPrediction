from pipeline.model_load_pipeline import model_loader_service


def main():
    mls = model_loader_service()
    mls.load_model()


if __name__ == '__main__':
    main()
