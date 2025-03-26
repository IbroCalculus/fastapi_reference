from typing import Optional, List

from fastapi import FastAPI, Response, Header

app = FastAPI()


@app.get("/")
# async def index(response: Response, custom_header : Optional[str] = Header(None)):
async def index(response: Response, custom_header: Optional[List[str]] = Header(None)):
    return {'message': 'return successfullyyy'}
