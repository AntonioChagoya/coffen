from fastapi import FastAPI
from model.db_connection import DBConnection
from schema.user_schema import UserSchema

app = FastAPI()
conn = DBConnection()


@app.get("/")
def index():
    conn
    return {"message": "Hello World"}


@app.get("/books/{book_id}")
def book_by_id(book_id: int):
    return {"book_id": book_id}


@app.post("/api/users")
def insert_user(user: UserSchema):
    data = user.dict()
    data.pop("id")
    conn.write(data)
    return {"message": "El libro ha sido insertado", "data": data}
