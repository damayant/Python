import json
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel


class Book(BaseModel):
    id:int
    title:str

library={}

def add_book_by_id(book:Book)->bool:
    if book.id not in library:
        library[book.id]=book
        return True
    return False

def get_all_books():
    return library

def delete_book_by_id(book:Book)->bool:
    if book.id in library:
        del library[book.id]
        return True
    return False

app=FastAPI()

@app.post("/books")
def add_book(request:Book):
    return add_book_by_id(request)

@app.get('/books')
def get_books():
    return get_all_books()

@app.delete('/books')
def delete_books(request:Book):
    return delete_book_by_id(request)

client=TestClient(app)

def test_adding_books():
    book1=Book(id=1,title="HP1")
    response=client.post('/books',json=book1.model_dump())
    # print(response,response.json())
    assert response.status_code==200

def test_get_books():
    response=client.get('/books')
    print(response.json())
    assert response.status_code==200

def test_delete_books():
    book=Book(id=1,title="HP1")
    response=client.request(
        method='DELETE',
        url='/books',
        json=book.model_dump()
    )
    assert response.status_code==200



test_adding_books()
test_get_books()
test_delete_books()
test_get_books()