from sqlalchemy import Column, Integer, Time
from app.database import Base


class Slot(Base):
    __tablename__ = 'slots'
    id = Column(Integer, primary_key=True, index=True)
    start_time = Column(Time, nullable=False, index=True)
    end_time = Column(Time, nullable=False, index=True)