import pandas as pd
from config import settings
from loguru import logger
from config import engine
from db_model import RentApartments
import sqlalchemy

@logger.catch

def load_data(path=settings.data_file_name):
    logger.info(f'loading csv file at path {path}')
    return pd.read_csv(path)

def load_data_from_db():
    logger.info("loading data table from database")
    query = sqlalchemy.select(RentApartments)
    return pd.read_sql(query, engine)
