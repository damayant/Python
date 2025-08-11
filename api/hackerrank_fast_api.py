from typing import Any, Dict
from fastapi.testclient import TestClient
import requests

BASE_URL="https://jsonmock.hackerrank.com/api/football_teams"

def get_all_football_teams():
    try:
        response=requests.get(BASE_URL)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching data:{str(e)}")
    
def get_football_by_page(page_number:int):
    try:
        response=requests.get(
            BASE_URL,
            params={"page_number":page_number}
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        raise RuntimeError(f"Error fetching data:{str(e)}")



from fastapi import FastAPI,HTTPException,status

app = FastAPI(title="Football Teams API", version="1.0.0")

@app.get('/teams')
def get_all_teams():
    return get_all_football_teams()

client=TestClient(app)

def test_get_teams():
    response=client.get('/teams')
    assert response.status_code==200
    

test_get_teams()



