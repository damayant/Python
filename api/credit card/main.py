from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.testclient import TestClient

def detect_card_type(card_number:str)->str:
    number=card_number.strip().replace(" ","")
    if not number.isdigit():
        return "Invalid"
    
    length=len(number)

    if number.startswith("4") and length in [13,16,19]:
        return "VISA"
    
    if length==16: 
        first_two=int(number[:2])
        first_four=int(number[:4])
        if 51<=first_two<=55 or 2221<=first_four<=2720:
            return "Mastercard"
    
    if length==15 and number.startswith(("34","37")):
        return "Amex"
    
    return "Unknown"


app=FastAPI(title="Credit Card Type Detector API")

class CardRequest(BaseModel):
    card_number:str 

class CardResponse(BaseModel):
    card_type:str 

@app.post("/detect",response_model=CardResponse)
def detect_card(request:CardRequest):
    card_type=detect_card_type(request.card_number)
    if card_type=="Invalid":
        raise HTTPException(
            status_code=422,
            detail="card number must contain only digits"
        )
    return {"card_type":card_type}

client=TestClient(app)

def test_credit_card():
    payload={"card_number": "4111111111111111"}
    response=client.post("/detect",json=payload)
    # print(response.json())
    assert response.status_code==200
    assert response.json()=={'card_type': 'VISA'}

test_credit_card()

def test_invalid_card():
    payload={"card_number":"abd1234"}
    response=client.post("/detect",json=payload)
    assert response.status_code==422
    assert response.json()["detail"] =="card number must contain only digits"

test_invalid_card()