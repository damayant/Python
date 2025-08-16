from sqlalchemy.orm import Session
from fastapi import HTTPException, status
import models, schema
import logging

logger=logging.getLogger(__name__)

#----helper-----#
def get_or_404(db_obj,obj_id:int,model_name:str):
    obj=db_obj.filter(models.Author.id==obj_id) if model_name=="Author" else db_obj.filter(models.Book.id==obj_id).first()
    if not obj:
        logger.warning(f"{model_name} with id:{obj_id} does not exist")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    return obj 

def commit_refresh(db:Session,obj):
    try:
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    except Exception as e:
        db.rollback()
        logger.exception(f"Database operation failed:{e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
#author---------------#
def create_author(db:Session, author:schema.AuthorBase):
    existing_author=db.query(models.Author).filter(models.Author.name==author.name).first()
    if existing_author:
        logger.warning(f"duplicate author creation. author {author.name} already exists")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST
        )
    author_data=author.model_dump()
    new_author=models.Author(**author_data)
    new_author=commit_refresh(new_author)
    logger.info(f"New author:{author.name} created")
    return new_author

def get_all_authors(db:Session):
    authors=db.query(models.Author).all()
    logger.info(f"{len(authors)} returned")
    return authors

def get_author_by_id(db:Session,author_id:int):
    author=get_or_404(db.query(models.Author),author_id,"Author")
    logger.info(f"returned author info")
    return author

def update_author(db:Session,author_id:int, author:schema.AuthorBase):
    existing_author=get_or_404(db.query(models.Author),author_id,"Author")
    update_data=author.model_dump(exclude_unset=True)
    for key,value in update_data.items():
        if hasattr(existing_author,key):
            setattr(existing_author,key,value)
    updated_author=commit_refresh(db,existing_author)
    return updated_author

def delete_author(db:Session,author_id:int):
    existing_author=get_or_404(db.query(models.Author),author_id,"Author")
    try:
        db.delete(existing_author)
        db.commit()
        logger.info()
    except Exception as e:
        db.rollback()
        logger.exception(f"Error deleting author:{e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


