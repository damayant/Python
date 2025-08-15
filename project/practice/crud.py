from sqlalchemy.orm import Session 
from fastapi import HTTPException, status 
import models, schema
import logging

logger=logging.getLogger(__name__)

def create_author(db: Session, name: str):
    #check if author already exist
    existing_author=db.query(models.Author).filter(models.Author.name==name).first()
    if existing_author:
        logger.warning(f"Attempt to create duplicate author:{name}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Author name {name} already exists"
        )
    try:
        db_author=models.Author(name=name)
        db.add(db_author)
        db.commit()
        db.refresh(db_author)
        logger.info(f"Author created: {db_author.id}-{db_author.name}")
        return {"id":db_author.id,"name":db_author.name}
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating author '{name}': {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error while creating author"
        )


def get_all_authors(db:Session):
    try:
        authors=db.query(models.Author).all()
        logger.info(f"{len(authors)} no of author details are returned")
        return authors
    except Exception as e:
        logger.error(f"Error occured while fetching Author records :{e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Error "
        )

def get_author_by_id(db:Session,author_id:int):
    author=db.query(models.Author).filter(models.Author.id==author_id).first()
    if not author:
        logger.warning(f"this {author_id} does not exist in Authors table")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{author_id} does not exist"
        )
    try:
        logger.info(f"author:{author_id} found")
        return {"id":author.id,"name":author.name}
    except Exception as e:
        logger.error(f"Error while fetching:{e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    
    
def delete_author(db:Session,author_id:int):
    author=get_author_by_id(db,author_id)
    if not author:
        logger.warning(f"this {author_id} does not exist in Authors table")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{author_id} does not exist"
        )
    try:
        db.delete(author)
        db.commit()
        logger.info(f"author:{author_id} deleted")
    except Exception as e:
        logger.error(f"Error while fetching:{e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )
    

# def update_author(db:Session,author_id:int):
#     author=db.query(models.Author).filter(models.Author.id==id).first()
#     if not author:
#         raise HTTPException(
#             status_code=status.HTTP_404_NOT_FOUND,
#             details=f'{author_id} does not exist'
#         )
#     try:
        
    