from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from database.db import SessionLocal
import pandas as pd

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()