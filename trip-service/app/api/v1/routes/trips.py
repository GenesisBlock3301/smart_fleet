from fastapi import APIRouter, Depends, HTTPException

router = APIRouter()

@router.get("/trips")
async def get_trips():
    return "Okay its working!"
