from fastapi import FastAPI, Response, Request, Form

app = FastAPI()

# pip install python-multipart

@app.get('/')
async def index():
    return {"message": "Welcome to form data!"}


@app.post("/login")
async def login(email: str = Form(...), password: str = Form(...)):
    return {'email': email, 'password': password}
