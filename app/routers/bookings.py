from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from datetime import date

from app.database import get_db
from app.models.booking import Booking, BookingStatus
from app.models.room import Room
from app.models.slot import Slot
from app.schemas.booking import BookingCreate, BookingResponse
from app.dependencies import get_current_user
from app.models.user import User

router = APIRouter(prefix="/bookings", tags=["bookings"])


@router.post("/", response_model=BookingResponse)
async def create_booking(
        booking_data: BookingCreate,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    existing = await db.execute(
        select(Booking).where(
            and_(
                Booking.room_id == booking_data.room_id,
                Booking.slot_id == booking_data.slot_id,
                Booking.booking_date == booking_data.booking_date,
                Booking.status == BookingStatus.ACTIVE
            )
        )
    )
    if existing.scalar_one_or_none():
        raise HTTPException(status_code=400, detail="Slot already booked")

    new_booking = Booking(
        room_id=booking_data.room_id,
        slot_id=booking_data.slot_id,
        booking_date=booking_data.booking_date,
        user_id=current_user.id,
        status=BookingStatus.ACTIVE
    )
    db.add(new_booking)
    await db.commit()
    await db.refresh(new_booking)
    return new_booking


@router.get("/my", response_model=list[BookingResponse])
async def my_bookings(
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    result = await db.execute(
        select(Booking).where(Booking.user_id == current_user.id)
    )
    return result.scalars().all()


@router.delete("/{booking_id}")
async def cancel_booking(
        booking_id: int,
        db: AsyncSession = Depends(get_db),
        current_user: User = Depends(get_current_user)
):
    result = await db.execute(select(Booking).where(Booking.id == booking_id))
    booking = result.scalar_one_or_none()

    if not booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    if booking.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not your booking")

    booking.status = BookingStatus.CANCELLED
    await db.commit()
    return {"message": "Booking cancelled"}