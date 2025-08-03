import pandas as pd
from config import settings
from loguru import logger
from config import engine
from db_model import RentApartments
import sqlalchemy

@logger.catch

def load_data_from_db():
    logger.info("loading data table from database")
    query = sqlalchemy.select(RentApartments)
    return pd.read_sql(query, engine)
