import pytest
from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from main import app
import crud,schema,models

@pytest.mark.parametrize("author_name",["Charles Diskens","X"])
def test_create_author_api(client:TestClient,db_session:Session,author_name):
    payload={"name":author_name}
    response=client.post("/authors/",json=payload)
    assert response.status_code==201
    data=response.json()
    assert data["name"]==author_name
    assert "id" in data

def test_create_duplicate_author(client:TestClient,db_session:Session):
    payload={"name":"Charles Dickens"}
    response=client.post("/authors/",json=payload)
    assert response.status_code==400 

def test_get_author_by_id(client:TestClient,db_session:Session):
    payload={"name":"Leo"}
    res= client.post("/authors/",json=payload)
    author_id=res.json()["id"]

    response=client.get(f"/authors/{author_id}")
    assert response.status_code==200
    data=response.json()
    assert data["name"]=="Leo"

def test_author_not_found(client:TestClient):
    response=client.get("/authors/999")
    assert response.status_code==404

def test_update_author(client:TestClient, db_session:Session):
    payload={"name":"XXX"}
    res=client.post("/authors/",json=payload)
    author_id=res.json()["id"]

    update_payload={"name":"TTT"}
    response=client.patch(f"/authors/{author_id}",json=update_payload)
    assert response.status_code==200
    data=response.json()
    assert data["name"]=="TTT"

def delete_author_by_id(client:TestClient,db:Session):
    payload={"name":"tobedeleted"}
    res=client.post("/authors/",json=payload)
    author_id=res.json()["id"]
    response=client.delete(f"/authors/{author_id}")
    assert response.status_code==204
