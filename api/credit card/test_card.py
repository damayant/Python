from fastapi.testclient import TestClient
from main import app

client=TestClient(app)

def test_api_detect_card():
    payload={"card_number": "4111111111111111"}
    response=client.post("/detect",json=payload)
    assert response.status_code==200
    assert response.json()=={"card_type":"Visa"}