import pandas as pd
import os
from collection import load_data
import re

def prepare_data():
    data = load_data()
    data_encoded = encode_cat_cols(data)
    data_encoded = parse_garden_col(data_encoded)
    return data_encoded

def encode_cat_cols(data):
    cat_features = ['balcony', 'storage', 'parking', 'furnished', 'garage']
    data_encoded = pd.get_dummies(data, columns=cat_features, drop_first=True)
    return data_encoded

def parse_garden_col(data):
    for i in range(len(data)):
        if data.garden[i]=='Not present':
            data.loc[i, 'garden'] = 0
        else: data.loc[i, 'garden'] = int(re.findall(r'\d+', data.garden[i])[0])

    return data