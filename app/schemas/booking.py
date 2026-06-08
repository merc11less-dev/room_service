from pydantic import BaseModel
from datetime import date, datetime
from enum import Enum

class BookingStatus(str, Enum):
    active = "active"
    cancelled = "cancelled"

class BookingBase(BaseModel):
    room_id: int
    slot_id: int
    booking_date: date
class BookingCreate(BookingBase):
    pass

class BookingResponse(BookingBase):
    id: int
    user_id: int
    status: BookingStatus
    created_at: datetime

    class Config:
        from_attributes = True