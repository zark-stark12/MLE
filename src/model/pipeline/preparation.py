import re

from loguru import logger
import pandas as pd

from model.pipeline.collection import load_data_from_db


@logger.catch

def prepare_data():
    logger.info("setting up preprocesing pipeline")
    data = load_data_from_db()
    data_encoded = encode_cat_cols(data)
    data_encoded = parse_garden_col(data_encoded)
    return data_encoded

def encode_cat_cols(data):
    cat_features = ['balcony', 'storage', 'parking', 'furnished', 'garage']
    logger.info(f"encoding categorical columns {cat_features}")
    data_encoded = pd.get_dummies(data, columns=cat_features, drop_first=True)
    return data_encoded

def parse_garden_col(data):
    logger.info("adding garden info value")
    for i in range(len(data)):
        if data.garden[i]=='Not present':
            data.loc[i, 'garden'] = 0
        else: data.loc[i, 'garden'] = int(re.findall(r'\d+', data.garden[i])[0])

    return data