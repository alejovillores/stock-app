from fastapi import FastAPI, status
from lib.version import Version
from config.database import Session

app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
async def read_root():
    return {"status": status.HTTP_200_OK, "version": Version().current()}
