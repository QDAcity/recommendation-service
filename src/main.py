# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from uuid import UUID
from core.Evaluation.EvalHandler import EvalHandler


TOKEN = ["0d95ba03-60b5-4626-91a7-34f0c9fe8414"]
MODEL_PATH = "./code_recommandation"

class Recommendation(BaseModel):
    token: UUID
    text: str


app = FastAPI()

origins = [
    "*"
]

# app.add_middleware(
#     CORSMiddleware,
#     allow_origins=origins,
#     allow_credentials=False,
#     allow_methods=["*"],
#     allow_headers=["*"],
# )

@app.get("/")
def read_root():
    return {"message": "Hello, World! FastAPI deployed!"}

@app.get("/recommendation")
async def get_recommendation(token: UUID, text: str):
    # data = data.model_dump()
    # print(data["token"])
    # print(data["token"]==TOKEN[0])
    valid_token = next( (token for token in TOKEN if str(token) == str(token)), None)
    valid_token = True
    if valid_token:
        handler = EvalHandler(model_path=MODEL_PATH)
        result = handler.predict(text)
        return  result
    else:
        return {"message": "Invalid token!"}
    