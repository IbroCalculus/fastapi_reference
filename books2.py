from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

BOOKS = []


class Book2:
    id: int
    title: str
    author: str
    category: str
    rating: int

    def __init__(self, id, title, author, category, rating):
        self.id = id
        self.title = title
        self.author = author
        self.category = category
        self.rating = rating

class Book(BaseModel):
    id: int = Field(description="The book's id number of integer value")
    title: str
    author: str
    category: str
    rating: int

    class Config:
        json_schema_extra = {
            "example": {
                "id": 99,
                "title": "Title 99",
                "author": "Author 99",
                "category": "Category 99",
                "rating": 9
            }
        }


BOOKS.append(Book(id=1, title="Title One", author="Author One", category="Category One", rating=7))
BOOKS.append(Book(id=2, title="Title Two", author="Author Two", category="Category Two", rating=9))
BOOKS.append(Book(id=3, title="Title Three", author="Author Three", category="Category Three", rating=3))
BOOKS.append(Book(id=4, title="Title Four", author="Author Four", category="Category Four", rating=6))


@app.get("/books")
def read_all_books():
    return BOOKS


@app.post("/create_book")
def create_book(new_book: Book):
    # the_book = Book(**new_book.model_dump())
    # print(f"DUMPED BOOK: {the_book}")
    BOOKS.append(new_book)
    return BOOKS
