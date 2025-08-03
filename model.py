from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from preparation import prepare_data
from sklearn.model_selection import GridSearchCV
import pandas as pd
import pickle
from config import settings
from loguru import logger
pd.options.mode.chained_assignment = None 

def build_model():
    logger.info("beginning model preprocessing of data")
    df = prepare_data()
    X,y = get_model_data(df)
    X_train, X_test, y_train, y_test= split_train_test(X, y)
    model = train_model(X_train, y_train)
    score = evaluate_model(model, X_test, y_test)
    print(score)
    save_model(model)
    

def get_model_data(data):
    logger.info("load model related data")
    IVs = ['area', 
       'construction_year', 
       'bedrooms', 
       'garden', 
       'balcony_yes', 
       'parking_yes', 
       'furnished_yes', 
       'garage_yes', 
       'storage_yes'
      ]

    X = data[IVs].copy()
    dv = data.rent.copy()
    return X, dv

def split_train_test(X, y):
    logger.info("build train test datasets")
    return train_test_split(X, y, test_size=0.2)

def train_model(X_train, y_train):
    logger.info("Training randomforest regressor model")
    grid_space = {'n_estimators': [100, 200, 300, 400, 500], 'max_depth': [3, 6, 9, 12, 15, 18, 21]}
    grid = GridSearchCV(RandomForestRegressor(), param_grid=grid_space, cv=5, scoring = 'r2')
    model_grid = grid.fit(X_train, y_train)

    return model_grid.best_estimator_

def evaluate_model(model, X_test, y_test):
    logger.info(f"evaluating model performance. SCORE={model.score(X_test, y_test)}")
    return model.score(X_test, y_test)

def save_model(model):
    logger.info(f"saving model to path: {settings.model_path}")
    pickle.dump(model, open(f'{settings.model_path}/{settings.model_name}', 'wb'))
