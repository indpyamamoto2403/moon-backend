from fastapi import FastAPI, Response
from fastapi.middleware.cors import CORSMiddleware
from get_response import get_response
import json

app = FastAPI()

# Define the CORS configuration to allow all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)

@app.get("/{endpoint}")
def read_root(endpoint: str):
    data = {"answer": get_response(endpoint)}
    json_data = json.dumps(data)
    return Response(content=json_data, media_type="application/json")
