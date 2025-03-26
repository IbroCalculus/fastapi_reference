from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()


# Instead of the default json response, returns HTML response
@app.get('/', response_class=HTMLResponse)
async def home():
    return """
    <h1>Home Page </h1>
    <p>This is paragraph one </p>
    <p>Here is paragraph two </p>
    """
