from datetime import datetime
from sqlalchemy import Integer, Date, DateTime, ForeignKey, Enum, Column, UniqueConstraint
from sqlalchemy.orm import relationship
from app.database import Base
import enum


class BookingStatus(str, enum.Enum):
    ACTIVE = "active"
    CANCELLED = "cancelled"


class Booking(Base):
    __tablename__ = 'bookings'
    id = Column(Integer, primary_key=True, index=True)
    booking_date = Column(Date, nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    status = Column(Enum(BookingStatus), default=BookingStatus.ACTIVE, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False, index=True)
    room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False, index=True)
    slot_id = Column(Integer, ForeignKey('slots.id'), nullable=False, index=True)


    __table_args__ = (
        UniqueConstraint('room_id', 'slot_id', 'booking_date', name='unique_booking'),
    )
