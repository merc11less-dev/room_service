from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.database import get_db
from app.models.room import Room
from app.schemas.room import RoomResponse
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/rooms", tags=["rooms"])


@router.get("/", response_model=list[RoomResponse])
async def get_rooms(
    db: AsyncSession = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Room))
    rooms = result.scalars().all()
    return rooms