from fastapi import FastAPI, File, UploadFile, HTTPException
from typing import List
from fastapi.responses import Response

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Working with filesss"}


# =========== 1. UPLOAD A SINGLE FILE AS BYTE ================
# Pros: Simple and straightforward for small text files.
# Cons: Not suitable for large files, and lacks access to file metadata

@app.post("/upload-byte-file/")  # .txt file
async def upload_byte_file(file: bytes = File(...)):
    content = file.decode('utf-8')
    return {"file_content": content}


# =========== 2. UPLOAD A SINGLE FILE AS UPLOAD ================
# Pros: Suitable for larger files, access to file metadata, and non-blocking file reading.
# Cons: Slightly more complex due to the use of UploadFile and asynchronous file reading.

@app.post("/upload-uploadfile/")
async def upload_upload_file(file: UploadFile = File(...)):
    content = await file.read()
    decoded_content = content.decode('utf-8')
    return {"file_content": decoded_content}


# =========== 3. UPLOAD MULTIPLE FILES ================
@app.post("/upload-files/")
async def upload_files(files: List[UploadFile] = File(...)):
    file_contents = []
    for file in files:
        try:
            content = await file.read()
            file_contents.append(content.decode("utf-8"))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error reading file {file.filename}: {str(e)}")
    return "\n\n".join(file_contents)
