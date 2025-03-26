from fastapi import FastAPI
from routers.first_api import first_router
from routers.second_api import second_router
from routers.blogpost import blogpost

app = FastAPI()

app.include_router(first_router.router)
app.include_router(second_router.router)
app.include_router(blogpost.router)
