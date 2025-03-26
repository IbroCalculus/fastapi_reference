from fastapi import FastAPI, Request
import time

app = FastAPI()

'''
Middleware in FastAPI is a powerful tool that allows you to modify or handle requests and responses globally for your entire application.
Middleware sits between the client making a request and the endpoint handling the request, allowing you to perform
operations both before the request reaches your endpoint and after the endpoint has generated a response.

* Middleware is applied globally, meaning it affects all incoming requests and outgoing responses in your FastAPI 
application.

A middleware function is defined as a callable that takes three parameters:

request: The incoming request object.
call_next: A function that will receive the request as an argument and return the response. It is used to pass control to the next middleware or the actual endpoint.
response: The response object returned by the call_next function.

The last middleware defined is the first to process the request and the last to process the response.

If you have dependencies with yield, the exit code will run after the middleware.
If there were any background tasks (documented later), they will run after all the middleware.
'''


# Third Middleware: Log start and end of processing
@app.middleware("http")
async def log_start_end(request: Request, call_next):
    print("Middleware 3 - Start processing request")
    response = await call_next(request)
    print("Middleware 3 - Finished processing request")
    return response


# Second Middleware: Add process time to response headers
@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    print("Middleware 2 - Request processing started")
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    print("Middleware 2 - Response received, processing time added")
    return response


# First Middleware: Log request method and URL path
@app.middleware("http")
async def log_request_data(request: Request, call_next):
    method = request.method
    url = request.url.path
    print(f"Middleware 1 - Request: {method} {url} - Processing started")
    response = await call_next(request)
    print(f"Middleware 1 - Request: {method} {url} - Response received")
    return response


@app.get('/')
async def home():
    time.sleep(5)
    print("Doneeee")
    return {'message': 'Welcome to this fast API project'}


'''
***************** CONSOLE OUTPUT: *****************
Middleware 1 - Request: GET / - Processing started
Middleware 2 - Request processing started
Middleware 3 - Start processing request
Doneeee
Middleware 3 - Finished processing request
Middleware 2 - Response received, processing time added
Middleware 1 - Request: GET / - Response received
'''
