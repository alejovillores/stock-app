from fastapi import FastAPI, status
from lib.version import Version
from config.database import Session


async def get_db():
    db = Session()
    try:
        yield db
    finally:
        db.close()


app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    return {"status": status.HTTP_200_OK, "version": Version().current()}
