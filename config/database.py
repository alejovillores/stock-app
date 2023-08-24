import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.log import get_logger


TEST_BD_URL = "sqlite:///data/test_app.db"

logging = get_logger(__name__)
load_dotenv()


def get_url():
    enviroment = os.getenv('ENV')
    if enviroment == 'development':
        db_url = os.getenv('DEV_BD_URL')
    elif enviroment == 'production':
        db_url = os.getenv('PROD_BD_URL')
    else:
        db_url = TEST_BD_URL
    return db_url


def get_session():
    try:
        db_url = get_url()
        logging.info(f'database url: {db_url}')
        engine = create_engine(db_url, echo=True)
        Session = sessionmaker(bind=engine)
        logging.info('engine and session created')
        return Session
    except:
        logging.error('could not create an engine or Session')
        raise Exception
