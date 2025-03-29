import time

from fastapi import FastAPI, HTTPException, Body
from pydantic import BaseModel

app = FastAPI()

list_of_books = []

@app.get('/')
async def home():
    return "Welcome to this API"


BOOKS = [
    {"title": "Title One", "author": "Author One", "category": "Science"},
    {"title": "Title Two", "author": "Author Two", "category": "Science"},
    {"title": "Title Three", "author": "Author Three", "category": "history"},
    {"title": "Title Four", "author": "Author Four", "category": "Math"},
    {"title": "Title Five", "author": "Author Five", "category": "Math"},
    {"title": "Title Six", "author": "Author Two", "category": "Math"}
]


@app.get('/books')
async def read_all_books():
    return BOOKS


@app.get('/books/')
async def read_book(book_name: str):
    print("{book_name} = ", book_name, end="\n")
    for book in BOOKS:
        print(f"book = {book}")
        if book['title'].casefold() == book_name.casefold():
            return book
    raise HTTPException(status_code=404, detail=f"The book '{book_name}' was not found.")


# http://127.0.0.1:8000/books/create_book. IN BODY: {"title": "Helmet Island", "author": "King Bouhad", "category": "Monarchy"}
@app.post('/books/create_book')
async def create_book(new_book_name = Body()):
    BOOKS.append(new_book_name)
    return BOOKS

# ======= ALTERNATIVE TO THE ABOVE IS USING A PYDANTIC BASEMODEL AS SHOWN BELOW ============

class Book(BaseModel):
    title: str
    author: str
    category: str


# http://127.0.0.1:8000/books/create_book. IN BODY: {"title": "Helmet Island", "author": "King Bouhad", "category": "Monarchy"}
@app.post('/books/create_book')
async def create_book(new_book_name: Book):
    BOOKS.append(new_book_name.model_dump())
    return BOOKS