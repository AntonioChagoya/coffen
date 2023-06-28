from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()


class Book(BaseModel):
    title: str
    author: str
    pages: int
    price: Optional[float]


@app.get("/")
def index():
    return {"message": "Hello World"}


@app.get("/books/{book_id}")
def book_by_id(book_id: int):
    return {"book_id": book_id}


@app.post("/books")
def insert_book(book: Book):
    return {"message": "El libro ha sido insertado", "data": book}
