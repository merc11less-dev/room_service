from pydantic import BaseModel
from datetime import time


class SlotBase(BaseModel):
    start_time: time
    end_time: time


class SlotCreate(SlotBase):
    pass


class SlotResponse(SlotBase):
    id: int

    class Config:
        from_attributes=True
