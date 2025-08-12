from pydantic import BaseModel, Field,validator 
from typing import List, Optional
from datetime import datetime

class ItemBase(BaseModel):
    title:str = Field(..., max_length=2000)
    description: Optional[str] = None
    price: float = Field(..., gt=0.0)

class ItemCreate(ItemBase):
    pass

class ItemUpdate(ItemBase):
    title: Optional[str] = None
    description: Optional[str] = None
    price: Optional[float] = None

class ItemInDB(ItemBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
        