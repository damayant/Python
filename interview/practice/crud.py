# app/crud.py
from sqlalchemy.orm import Session
from typing import List, Optional, Tuple
from . import models, schemas
from sqlalchemy import select

def create_item(db: Session, item_create: schemas.ItemCreate) -> models.Item:
    item = models.Item(**item_create.dict())
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def get_item(db: Session, item_id: int) -> Optional[models.Item]:
    return db.query(models.Item).filter(models.Item.id == item_id).first()

def get_items(db: Session, limit: int = 50, offset: int = 0, q: Optional[str] = None) -> Tuple[List[models.Item], int]:
    query = db.query(models.Item)
    if q:
        query = query.filter(models.Item.title.ilike(f"%{q}%"))
    total = query.count()
    items = query.order_by(models.Item.id.desc()).offset(offset).limit(limit).all()
    return items, total

def update_item(db: Session, item: models.Item, patch: schemas.ItemUpdate) -> models.Item:
    data = patch.dict(exclude_unset=True)
    for key, val in data.items():
        setattr(item, key, val)
    db.add(item)
    db.commit()
    db.refresh(item)
    return item

def delete_item(db: Session, item: models.Item) -> None:
    db.delete(item)
    db.commit()