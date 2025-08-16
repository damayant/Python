from pydantic import BaseModel
from typing import List , Optional 

class AuthorBase(BaseModel):
    name:str 

class AuthorCreate(AuthorBase):
    pass 

class BookBase(BaseModel):
    title:str 
    genre:Optional[str]=None 
    author_id:Optional[int]=None

class BookCreate(BookBase):
    pass 
class BookUpdate(BookBase):
    pass 
