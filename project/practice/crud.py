from sqlalchemy.orm import Session 
from fastapi import HTTPException, status 
import models, schema
import logging

logger=logging.getLogger(__name__)

def create_author(db: Session, author:schema.AuthorBase):
    #check if author already exist
    existing_author=db.query(models.Author).filter(models.Author.name==author.name).first()
    if existing_author:
        logger.warning(f"Attempt to create duplicate author:{author.name}")
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Author name {author.name} already exists"
        )
    try:
        author_data=author.model_dump() #convert pydantic to dict
        new_author=models.Author(**author_data)
        db.add(new_author)
        db.commit()
        db.refresh(new_author)
        logger.info(f"Author created: {new_author.id}-{new_author.name}")
        return author
    except Exception as e:
        db.rollback()
        logger.error(f"Error creating author '{author.name}': {e}")
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
    author=db.query(models.Author).filter(models.Author.id==author_id).first()
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
    

def update_author(db:Session,author_id:int,author_data:schema.AuthorBase):
    author=db.query(models.Author).filter(models.Author.id==author_id).first()
    if not author:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'{author_id} does not exist'
        )
    try:
        update_data=author_data.model_dump(exclude_unset=True)
        for key,value in update_data.items():
            if hasattr(author,key):
                setattr(author,key,value)
        db.commit()
        db.refresh(author)
        return author
    except Exception as e:
        logger.error(f"Error while fetching:{e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Internal server error {e}"
        )
        
def add_book(db:Session, book:schema.BookBase):
    existing_book=db.query(models.Book).filter(models.Book.title==book.title).first()
    book_author_id=db.query(models.Author).filter(models.Author.id==book.author_id).first()
    if existing_book or book_author_id is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"This book already exists:{book.title}/ this author {book.author_id} does not exist"
        )
 

    try:
        book_data=book.model_dump() #convert pydantic into dict
        new_book=models.Book(**book_data)#unpack dict into SQLAlchemy model
        db.add(new_book)
        db.commit()
        db.refresh(new_book)
        logger.info(f"{new_book} is created")
        return new_book
    except Exception as e:
        db.rollback()
        logger.exception(f"error occured while adding book:{e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

def get_books(db:Session):
    books=db.query(models.Book).all()
    if not books:
        logger.warning(f"No books found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    try:
        logger.info(f"{len(books)} books found")
        return books
    except Exception as e:
        logger.exception(f"Error while fetching all books:{e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    
def delete_book_by_id(db:Session,book_id:int):
    book=db.query(models.Book).filter(models.Book.id==book_id).first()
    if not book:
        logger.warning(f"book with id:{book_id} not found")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    try:
        db.delete(book)
        db.commit()
        logger.info(f"book id:{book_id} deleted")
    except Exception as e:
        db.rollback()
        logger.exception(f"error while deleteing book id:{book_id}: {e}")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    
def update_book(db:Session,book:schema.BookBase):
    existing_book=db.query(models.Book).filter(models.Book.title==book.title).first()
    if not existing_book:
        logger.warning(f"This book : {book.title} does not exist")
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND
        )
    try:
        update_book=book.model_dump(exclude_unset=True)
        for key,value in update_book.items():
            if hasattr(existing_book,key):
                setattr(existing_book,key,value)
        logger.info(f"book:{book.title} is updated")
        return book 
    except Exception as e:
        logger.exception(f"error while updating book:{book.id}:{e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
    