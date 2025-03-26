from fastapi import FastAPI, status
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
from sqlmodel import SQLModel, Session, select
from models import Category
from database import engine
from typing import List

app = FastAPI()
session = Session(bind=engine)


@app.get('/', response_class=HTMLResponse)
async def home():
    return """
    <h1>Home Page </h1>
    <p>This is paragraph one </p>
    <p>Here is paragraph two </p>
    """


# Get all categories
@app.get('/categories/', response_model=List[Category])
async def get_all_categories():
    with Session(engine) as session:
        statement = select(Category)
        result = session.exec(statement)
        all_categories = result.all()
    return all_categories


# Post a new category
@app.post('/categories/', status_code=status.HTTP_201_CREATED)
async def post_a_category(category:Category):
    new_category = Category(name=category.name)
    with Session(engine) as session:
        # See if that category name is already in the table
        statement = select(Category).where(Category.name == category.name)
        # Reject if name already exists
        if session.exec(statement).one_or_none():
            return HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Category name already in use")
        session.add(new_category)
        session.commit()
        session.refresh(new_category)
    return new_category


# Get one category
@app.get('/category/{category_id}')
async def get_a_category(category_id: int):
    pass


# Update one category
@app.put('/category/{category_id}')
async def update_a_category(category_id: int):
    pass


# Delete one category
@app.delete('/category/{category_id}')
async def delete_a_category(category_id: int):
    pass
