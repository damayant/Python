from pydantic import BaseModel
from typing import List, Optional 

class Item(BaseModel):
    name:str 
    description:Optional[str]=None 
    price:float


class ItemResponse(Item):
    id:int 

ITEMS={}
NEXT_ID=1

def create_item(item:Item)->bool:
    if item['id'] not in ITEMS:
        ITEMS[id]=item
        return True 
    return False

def get_all_items():
    return ITEMS 

def update_item(item_id:int,item:Item):
    for i,existing in enumerate(ITEMS):
        if existing['id']==item_id
            ITEMS[i]=item 
            return item 
    return None 

def delete_item(item_id:int)->bool:
    if item_id in ITEMS:
        del ITEMS[item_id]
        return True
    return False
