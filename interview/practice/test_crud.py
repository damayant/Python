# tests/test_crud.py
from app import crud, schemas
from app.models import Item

def test_create_and_get_item(db_session):
    item_in = schemas.ItemCreate(title="Test", description="desc", price=12.5)
    item = crud.create_item(db_session, item_in)
    assert item.id is not None
    assert item.title == "Test"

    fetched = crud.get_item(db_session, item.id)
    assert fetched.id == item.id

def test_update_and_delete(db_session):
    item_in = schemas.ItemCreate(title="Old", description=None, price=1.0)
    item = crud.create_item(db_session, item_in)

    patch = schemas.ItemUpdate(title="New", price=2.5)
    updated = crud.update_item(db_session, item, patch)
    assert updated.title == "New"
    assert updated.price == 2.5

    crud.delete_item(db_session, updated)
    assert crud.get_item(db_session, updated.id) is None