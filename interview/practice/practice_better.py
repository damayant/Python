import logging
from fastapi import FastAPI
from fastapi.testclient import TestClient
from pydantic import BaseModel

GLOBAL_INDEX=0
library={}

class Book(BaseModel):
    id:int
    title:str 


def add_book_by_id(book:Book)->bool:
    global GLOBAL_INDEX
    if book.id not in library:
        library[book.id+GLOBAL_INDEX]=book 
        logging.info(f"Book added:{book}")
        GLOBAL_INDEX+=1
        return True
    logging.info(f"Book {book} already exists")
    return False 

app=FastAPI()

@app.post('/books')
def add_book(request:Book):
    return add_book_by_id(request)


client=TestClient(app)

book1=Book(id=1,title="HP1")
book2=Book(id=2,title="HP2")
book3=Book(id="a",title=1)


def test_book_model_validate(book:Book):
    assert isinstance(book.id,int)
    assert isinstance(book.title,str)


test_book_model_validate(book1)