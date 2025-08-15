from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Author(Base):
    __tablename__="authors"
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String,nullable=False,unique=True)

class Book(Base):
    __tablename__="books"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String,nullable=False)
    genre=Column(String)
    author_id=Column(Integer)