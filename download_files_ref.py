from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
import os

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Downloading files'}


# http://127.0.0.1:8000/download/lambo1.jpeg
@app.get('/download/{filename}')
async def download_file(filename: str):
    file_path = f'some_files/{filename}'
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")
    return FileResponse(path=file_path, filename=filename)
