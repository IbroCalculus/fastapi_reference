from fastapi import FastAPI
from routers import user

from db import models
from db.database_conn import engine

app = FastAPI()
app.include_router(user.router)


@app.get('/')
async def root():
    return {"message": "Hello, World!"}


models.Base.metadata.create_all(bind=engine)
