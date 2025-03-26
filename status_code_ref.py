from fastapi import FastAPI, status

app = FastAPI()


@app.get('/', status_code=status.HTTP_201_CREATED)     # If successful, return 201 instead of default 200
async def home():
    return {'message': 'This is the response'}
