# https://fastapi.tiangolo.com/ko/

# http://localhost:8000/item-by-name?name=bread
# http://localhost:8000/items/0?q=123
# http://localhost:8000/item/0/name
# http://localhost:8000/docs
# http://localhost:8000/redoc

# 설치
# pip install fastapi
# pip install "uvicorn[standard]"

# 실행
# uvicorn main:app --reload

from typing import Union

from fastapi import FastAPI

app = FastAPI()

'''
CRUD : Create, Read, Update, Delete
@app.post
'''

items = {
  0: {"name": "bread", "price": 1000},
  1: {"name": "bread1", "price": 2000},
  2: {"name": "bread2", "price": 3000},
}

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
# item_id 는 파라미터 타입을 정의해주는 것이고, q 는 쿼리스트링
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": items[item_id], "q": q}

@app.get("/item/{item_id}/{item_name}")
def read_item(item_id: int, item_name: str):
    return {"item": items[item_id][item_name]}

@app.get("/item-by-name")
def read_item_by_name(name: str):
  for item_id, item in items.items():
    if item["name"] == name:
      return {"item_id": item_id, "item": item}
  return {"message": "not found"}