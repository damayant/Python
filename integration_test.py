# tests/test_api_integration.py
import pytest

def test_full_item_lifecycle(client):
    # create
    res = client.post("/items", json={"title":"API Item","description":"via api","price":9.99})
    assert res.status_code == 201
    payload = res.json()
    item_id = payload["id"]
    assert payload["title"] == "API Item"

    # read
    res = client.get(f"/items/{item_id}")
    assert res.status_code == 200
    assert res.json()["title"] == "API Item"

    # patch
    res = client.patch(f"/items/{item_id}", json={"price": 19.99})
    assert res.status_code == 200
    assert res.json()["price"] == 19.99

    # list
    res = client.get("/items")
    assert res.status_code == 200
    assert isinstance(res.json(), list)

    # delete
    res = client.delete(f"/items/{item_id}")
    assert res.status_code == 204

    # confirm gone
    res = client.get(f"/items/{item_id}")
    assert res.status_code == 404