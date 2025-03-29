from fastapi import FastAPI, Body
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
def init():
    return {'message': 'This is the initial request'}

class Book(BaseModel):
    title: str
    author: str
    category: str

BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Two", "category": "Math"}
]

@app.get("/get_book/{book_title}")
def get_book(book_title: str):
    for book in BOOKS:
        if book["title"] == book_title:
            return {"response": book}
    return {"response": f"{book_title} does not exist"}


@app.get("/get_book2/")
def get_book(book_title2: str):
    for book in BOOKS:
        if book["title"] == book_title2:
            return {"response": book}
    return {"response": f"{book_title2} DOES not exist"}

@app.post("/create_book")
def create_book(book: Book):
    BOOKS.append(book.model_dump())
    return BOOKS


@app.post("/create_book2")
def create_book2(book2 = Body()):
    BOOKS.append(book2)
    return BOOKS