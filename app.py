import typing

from fastapi import FastAPI, status, Body
from pydantic import BaseModel


class Item(BaseModel):
    item_id: typing.Union[str, int]
    item_name: str
    item_bool: bool
    
class ItemDetail(BaseModel):
    item_color: str
    item_detail: str
    
app = FastAPI()

@app.get("/")
def root():
    return ({"msg": "welcome to root page"})


@app.get("/items/{item_id}/{item_name}")
def show_item(item_id: typing.Union[str, int], item_name: str):
    return ({"item_id": item_id , "item_name": item_name})


@app.post("/items", status_code=status.HTTP_201_CREATED)
def create_item():
    return ({"msg": "created"})


@app.get("/items")
def query_item(item_id: int = 1, item_name: str= "foo", item_bool: typing.Union[bool, None] = None):
    if item_bool:
        return ({"item_id": item_id , "item_name": item_name, "item_bool": item_bool})
    return ({"item_id": item_id , "item_name": item_name})


@app.get("/items/with_body")
def show_item_body(item: Item): #, detail: ItemDetail):
    return {"item": item}#, "detail": detail})

@app.get("/items/combine/{item_id}")
def combine_all_params(item_id: str, item_name: str, item_detail: ItemDetail):
    return {"item_id": item_id, "item_name": item_name, "item_detail": item_detail}