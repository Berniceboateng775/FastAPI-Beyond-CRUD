from fastapi import FastAPI, Header, status
from typing import Optional, List
from pydantic import BaseModel

app = FastAPI()

books = [ 
    {
        "id": 1,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publisher": "Scribner",
        "published_date": "1925-04-10",
        "page_count" : 1234,
        "language": "English"
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "publisher": "J. B. Lippincott & Co.",
        "published_date": "1960-07-11",
        "page_count" : 281,
        "language": "English"
    },
    {
        "id": 3,
        "title": "Ruthless People",
        "author": "J.J McAvoy",
        "publisher": "J.J McAvoy",
        "published_date": "2015-05-10",
        "page_count" : 328,
        "language": "English"
    },
    {
        "id": 4,
        "title": "The Catcher in the Rye",
        "author": "J. D. Salinger",
        "publisher": "Little, Brown and Company",
        "published_date": "1951-07-16",
        "page_count" : 277,
        "language": "English"
    },
    {
        "id": 5,
        "title": "Handsome Devil",
        "author": "L.J Shen",
        "publisher": "L.J Shen",
        "published_date": "2016-05-10",
        "page_count" : 300,
        "language": "English"
    }
]

class Book(BaseModel):
    id: int
    title: str
    author: str
    publisher: str
    published_date: str
    page_count: int
    language: str

@app.get("/books",response_model=List[Book])
async def get_all_books():
    return books

@app.post("/books", status_code=status.HTTP_201_CREATED)
async def create_a_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return {"message": "Book created successfully", "book": new_book}

@app.get("/books/{book_id}")
async def get_a_book(book_id: int) -> dict:
    pass

@app.put("/books/{book_id}")
async def update_a_book(book_id: int) -> dict:
    pass

@app.delete("/books/{book_id}")
async def delete_a_book(book_id: int) -> dict:
    pass