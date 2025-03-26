

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from typing import Optional, List

"""
    - BaseModel class
"""

app = FastAPI()


# Field() -> They allow adding extra validations to class variables

class Book(BaseModel):
    id: Optional[UUID] = uuid4()
    title: str
    author: str                      # author: str = Field(min_length=10)
    description: Optional[str] = ""  # description: Optional[str] = Field(title:"Description of the book", min_length=1, max_length=50)
    rating: int = Field(gt=0)

    class Config:
        json_schema_extra: {
            "example": {
                "title": "titleOne",
                "author": "authorOne",
                "description": "descriptionOne",
                "rating": 6
            }
        }

BOOKS: List[Book] = [
    Book(
        title="titleOne",
        author="authorOne",
        description="descriptionOne",
        rating=6
    ),
    Book(
        title="titleTwo",
        author="authorTwo",
        description="descriptionTwo",
        rating=8
    )
]

# ============ POST operation ===========
@app.post("/create-book/")
async def createBook(book: Book):
    the_book = Book(**book.model_dump())      # RETURNS OUTPUT AS SUCH: id=5 title='Title Five' author='Author Five' category='Category Five' rating=6
    BOOKS.append(book)
    return BOOKS


# ============ PUT operation for updating a book ===========
@app.put("/update-book/{book_id}")
async def update_book(book_id: UUID, updated_book: Book):
    for book in BOOKS:
        if book.id == book_id:
            # Update the existing book with the new values
            BOOKS.remove(book)
            BOOKS.append(updated_book)
            return {"message": f"Book with ID {book_id} updated successfully"}

    # If the book with the given ID is not found, raise an HTTPException
    raise HTTPException(status_code=404, detail=f"Book with ID {book_id} not found")

@app.get("/")
async def read_data():
    return BOOKS
