from fastapi import FastAPI, Response
import json

app = FastAPI()

@app.get("/")
def read_root():
    data = {"Hello": "sir"}
    json_data = json.dumps(data)
    return Response(content=json_data, media_type="application/json")

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
    data = {"item_id": item_id, "q": q}
    json_data = json.dumps(data)
    return Response(content=json_data, media_type="application/json")