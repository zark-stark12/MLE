from model_service import ModelService

from loguru import logger

@logger.catch
def main():
    ml_svc = ModelService()
    ml_svc.load_model()

    input_params = [85, 2015, 2, 20, 1, 1, 0, 0, 1]
    pred = ml_svc.predict(input_params)
    print(pred)

if __name__ == '__main__':
    main()