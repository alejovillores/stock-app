import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.log import get_logger

logging = get_logger(__name__)
load_dotenv()

try:
    enviroment = os.getenv('ENV')
    if enviroment == 'development':
        db_url = os.getenv('DEV_BD_URL')
    elif enviroment == 'production':
        db_url = os.getenv('PROD_BD_URL')
    else:
        db_url = os.getenv('TEST_BD_URL')

    logging.info(f'database url: {db_url}')
    engine = create_engine(db_url, echo=True)
    Session = sessionmaker(bind=engine)
    logging.info('engine and session created')
except:
    logging.error('could not create an engine or Session')
    raise Exception
