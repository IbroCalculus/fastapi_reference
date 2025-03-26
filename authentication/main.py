from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastAPI.authentication.oauth2_ref import oauth2_scheme

app = FastAPI()


@app.get('/')
def index(token: str = Depends(oauth2_scheme)):
    return {'message': 'endpoint authentication'}


@app.post('/token/')
async def get_token(request: OAuth2PasswordRequestForm = Depends()):
    pass
