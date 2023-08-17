from fastapi import FastAPI, status
from ..lib.version import Version


app = FastAPI()


@app.get("/", status_code=status.HTTP_200_OK)
def read_root():
    return {"status": status.HTTP_200_OK, "version": Version().current()}
