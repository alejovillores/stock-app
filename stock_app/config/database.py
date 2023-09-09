import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .log import get_logger
from .constants import TEST_BD_URL, DEV_BD_URL, PROD_BD_URL


logging = get_logger(__name__)
load_dotenv()


def get_url():
    enviroment = os.getenv("ENV")
    if enviroment == "development":
        db_url = DEV_BD_URL
    elif enviroment == "production":
        db_url = PROD_BD_URL
    else:
        db_url = TEST_BD_URL
    return db_url


def get_session():
    try:
        db_url = get_url()
        logging.info(f"database url: {db_url}")
        engine = create_engine(db_url, echo=True)
        LocalSession = sessionmaker(bind=engine)
        logging.info("engine and session created")
        return LocalSession
    except Exception as e:
        logging.error("could not create an engine or Session")
        raise e
