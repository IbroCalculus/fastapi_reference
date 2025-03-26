from fastapi import FastAPI
from db import models
from db.database import engine

app = FastAPI()


@app.get('/')
def root():
    return {'message': 'Instagram Clone API'}


models.Base.metadata.create_all(engine)
