from fastapi import APIRouter, HTTPException

router = APIRouter()

@router.get('/')
async def test_api():
    return {"Greatings": "Hello World"}