from loguru import logger
import sqlalchemy
import pandas as pd

from config import engine
from db.db_model import RentApartments
@logger.catch

def load_data_from_db():
    logger.info("loading data table from database")
    query = sqlalchemy.select(RentApartments)
    return pd.read_sql(query, engine)
