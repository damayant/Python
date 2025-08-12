# app/main.py
from fastapi import FastAPI, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List
from . import models, schemas, crud
from .database import engine, Base
from .deps import get_db

# Create DB tables on startup for demo purposes. In prod use migrations (alembic).
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Senior CRUD API", version="0.1")

@app.post("/items", response_model=schemas.ItemOut, status_code=status.HTTP_201_CREATED)
def create_item_endpoint(item_in: schemas.ItemCreate, db: Session = Depends(get_db)):
    return crud.create_item(db, item_in)

@app.get("/items", response_model=List[schemas.ItemOut])
def list_items(q: str = Query(None, description="search in title"), limit: int = 50, offset: int = 0, db: Session = Depends(get_db)):
    items, _ = crud.get_items(db, limit=limit, offset=offset, q=q)
    return items

@app.get("/items/{item_id}", response_model=schemas.ItemOut)
def get_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.patch("/items/{item_id}", response_model=schemas.ItemOut)
def patch_item_endpoint(item_id: int, patch: schemas.ItemUpdate, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return crud.update_item(db, item, patch)

@app.delete("/items/{item_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_item_endpoint(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_item(db, item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    crud.delete_item(db, item)
    return None