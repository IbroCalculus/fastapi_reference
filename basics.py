
# FastApi uses the uvicorn http server. It's an asynchronous server
# pip install "fastapi[standard]"
# pip install "uvicorn[standard]"

# Run the server with:
# Open the .python file path in terminal, then run the below command
#   To start server: uvicorn main:app --reload      (Replace "main" with python file name. ie; uvicorn http_request_methods:app --reload)
#   To start server: uvicorn main:app --reload --port 8005  (For custom port number, ie 8005)
#   To stop running server: Ctrl+C
# Open your browser at http://127.0.0.1:8000/
# Open your browser at http://127.0.0.1:8000/docs   -> To get the auto documentation of my API Using Swagger UI
# Open your browser at http://127.0.0.1:8000/redoc  -> Using Redoc

# ALTERNATIVE RUN COMMANDS (Using FastAPI CLI. NB: Using Uvicorn above is the recommended)
# fastapi dev main.py --port 8002       (In development mode)
# fastapi run main.py --port 8002       (In production mode)


'''
    ----------------- To change port from 8080; do as follows at the bottom of the file: -----------------

import uvicorn
from fastapi import FastAPI

app = FastAPI()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=9000)

'''
