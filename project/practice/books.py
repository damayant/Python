from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import crud,schema,database
import logging

logger=logging.getLogger(__name__)
router=APIRouter(prefix="/books")

@router.post("/",status_code=201)
def add_book(book:schema.BookCreate, db:Session=Depends(database.get_db)):
    return crud.add_book(db,book)

@router.get("/",status_code=200)
def get_books(db:Session=Depends(database.get_db)):
    return crud.get_books(db)

@router.delete("/{book_id}",status_code=204)
def delete_book(book_id:int,db:Session=Depends(database.get_db)):
    return crud.delete_book_by_id(db,book_id)

@router.patch("/",status_code=200)
def update_book(book:schema.BookBase,db:Session=Depends(database.get_db)):
    return crud.update_book(db,book)