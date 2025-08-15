from sqlalchemy.orm import Session 
from fastapi import HTTPException, status 
import models, schema
import logging

def create_author(db: Session, name: str):
    db_author = models.Author(name=name)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author

def get_all_authors(db:Session):
    authors= db.query(models.Author).all()
    return [{"id":author.id,"name":author.name} for author in authors]

def get_author(db:Session,author_id:int):
    db.query(models.Author).filter(models.Author.id==author_id).first()
    
def delete_author(db:Session,author_id:int):
    author=get_author(db,author_id)
    db.delete(author)
    db.commit()

def delete_all_author(db:Session):
    db.delete(models.Author).all()
    