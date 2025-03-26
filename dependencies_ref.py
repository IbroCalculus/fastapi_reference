from fastapi import FastAPI, Depends

app = FastAPI()


def my_dependencies():
    return {"dependencyy": "This is just a dependency function"}


@app.get('/')
def index():
    return {"message": "Hello, World!"}


@app.get('/dep')
def dependent_route(my_dep: dict = Depends(my_dependencies)):
    return {"message": f"Hello!", 'my_dep': my_dep}
