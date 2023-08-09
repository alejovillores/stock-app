from typing import Union
from fastapi import FastAPI, status
import version


app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {
        "status":status.HTTP_200_OK,
        "version": version.get_version()
    }