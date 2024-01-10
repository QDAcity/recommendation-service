# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "*"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"message": "Hello, World! FastAPI deployed!"}

@app.get("/recommendation")
def get_recommendation(doc: str):
    return {"message": "Recommendation endpoint!"}

@app.get("/recommendation/{id}")
def get_recommendation_by_id(id: int):
    return {"message": f"Recommendation endpoint with id {id}!"}

@app.post("/recommendation")
def post_recommendation():
    return {"message": "Recommendation endpoint!"}

@app.put("/recommendation/{id}")
def put_recommendation(id: int):
    return {"message": f"Recommendation endpoint with id {id}!"}

@app.delete("/recommendation/{id}")
def delete_recommendation(id: int):
    return {"message": f"Recommendation endpoint with id {id}!"}

@app.get("/recommendation/{id}/similar")
def get_similar_recommendation(id: int):
    return {"message": f"Recommendation endpoint with id {id}!"}

## all of the docuemts