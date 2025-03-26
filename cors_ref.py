from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS : Cross Origin Resource Sharing
'''
CORS or "Cross-Origin Resource Sharing" refers to the situations when a frontend running in a browser has JavaScript 
code that communicates with a backend, and the backend is in a different "origin" than the frontend.

An origin is the combination of protocol (http, https), domain (myapp.com, localhost, localhost.tiangolo.com), 
and port (80, 443, 8080).

So, all these are different origins:

http://localhost
https://localhost
http://localhost:8080
'''


app = FastAPI()

# Define the origins that should be allowed to make requests to your API
origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://example.com",  # Replace with your frontend's origin
]
# origins = ['*']  # Allows all origins to be allowed


# Add the CORS middleware to the FastAPI application
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  # Allows requests from the listed origins
    allow_credentials=True,  # Allows cookies to be included in requests
    allow_methods=["*"],  # Allows all HTTP methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)


@app.get('/')
async def index():
    return {"message": "Learning about cors"}
