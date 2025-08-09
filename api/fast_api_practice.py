from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.testclient import TestClient

app=FastAPI()

class User(BaseModel):
    id:int 
    name:str 


users=[User(id=1,name="Alice")]

@app.get("/users")
def get_users():
    return users 

@app.post("/users",status_code=201)
def create_user(user:User):
    users.append(user)
    return user 


client=TestClient(app)
def test_get_user():
    res=client.get("/users")
    assert res.status_code==200
    assert isinstance(res.json(),list)


def test_create_and_fetch_user():
    new_user={"id":2,"name":"Bob"}
    post_res=client.post("/users",json=new_user)
    assert post_res.status_code==201

    get_res=client.get("/users")
    assert new_user in get_res.json()

test_get_user()
test_create_and_fetch_user()
new_user={"id":4,"name":"JACK"}
client.post("/users",json=new_user)
print(client.get("/users").json())