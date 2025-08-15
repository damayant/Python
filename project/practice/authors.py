from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
import crud,schema,database
import logging

logger=logging.getLogger(__name__)
router=APIRouter(prefix='/authors')

@router.post("/",status_code=201)
def create_author(author: schema.AuthorCreate,db:Session=Depends(database.get_db)):
    logger.info(f"Recieved request to create author: {author.name}")
    return crud.create_author(db, author.name)

@router.get("/",status_code=200)
def get_authors(db:Session=Depends(database.get_db)):
    logger.info(f"Generating view of authors table")
    return crud.get_all_authors(db)

@router.delete("/{author_id}",status_code=204)
def delete_author(author_id:int,db:Session=Depends(database.get_db)):
    logger.info(f"Deleting author:{author_id}")
    crud.delete_author(db,author_id)

@router.delete("/",status_code=204)
def delete_all_authors(db:Session=Depends(database.get_db)):
    crud.delete_all_author(db)