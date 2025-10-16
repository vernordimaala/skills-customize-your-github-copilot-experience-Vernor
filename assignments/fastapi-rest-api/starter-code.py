from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Item(BaseModel):
    name: str
    description: str

items: List[Item] = []

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI REST API assignment!"}

@app.get("/items")
def get_items():
    return items

@app.post("/items")
def create_item(item: Item):
    items.append(item)
    return item
