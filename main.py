from fastapi import FastAPI
from database.db import Base, engine

app = FastAPI()

app.get("/")
async def root():
    return {"message": "Welcome to the ML API"}