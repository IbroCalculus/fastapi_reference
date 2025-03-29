import uvicorn
from fastapi import FastAPI
import hashlib

app = FastAPI()

@app.get("/")
def home():
    return {"msg" : "Welcome to the home of this API", "url" : "http://demo.fastapi.com"}

@app.get("/hello")
def home():
    return {"msg" : "This is a hellow message endpoint"}



@app.get("/generate_sha256",)
def generate_sha256(input_string) -> dict:
    sha256_hash = hashlib.sha256()
    sha256_hash.update(input_string.encode('utf-8'))
    return {"Generated hash" : sha256_hash.hexdigest()}