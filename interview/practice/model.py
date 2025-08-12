from sqlalchemy import Column, Integer, String, Text, Float, DateTime
from sqlalchemy.sql import func
from .database import Base

class Item(Base):
    __tablename__="items"
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String(2000),nullable=False,index=True)
    description = Column(Text, nullable=True)
    price = Column(Float, nullable=False, default=0.0)
    created_at = Column(DateTime(timezone=True), server_default=func.now())