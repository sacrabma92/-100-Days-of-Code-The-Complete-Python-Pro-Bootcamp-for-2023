from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Item(BaseModel):
  name: str
  price: float
  is_offer: Union[bool, None] = None

@app.get('/')
def read_root():
  return {'Hello':'World!!!'};

@app.get('/hola')
def hola_mundo():
  return {'Hola Mundo'}

@app.get('/items/{id}')
def read_item(id: int, q: Union[str, None] = None):
  return {"item_id": id, "q": q}

@app.get('/suma')
def suma(num1: float, num2: float):
  return {"suma": num1 + num2}

@app.put('/items/{item_id}')
def uptate_item(item_id: int, item: Item):
  return {"item_name":item.name, "item_id": item_id, "item_price":item.price}