from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def home():
    return 'Just returning a text for home'
