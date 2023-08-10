import os
from sqlalchemy import create_engine

try:
    enviroment = os.getenv('ENV')
    if enviroment == 'development':
        db_url = os.getenv('DEV_BD_URL')
    elif enviroment == 'production':
        db_url = os.getenv('PROD_BD_URL')
    else:
        db_url = os.getenv('TEST_BD_URL')
    engine = create_engine(db_url, echo=True )
except:
    raise Exception