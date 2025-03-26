from fastapi import Depends, FastAPI

app = FastAPI()


# Define a dependency
def common_parameters(q: str = None, limit: int = 10):
    return {"q": q, "limit": limit}


# url: http://127.0.0.1:8000/items/?q=Hello&limit=100
@app.get("/items/")
async def get_items(params: dict = Depends(common_parameters)):
    return {"params": params}
