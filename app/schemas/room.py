from pydantic import BaseModel


class RoomBase(BaseModel):
    name: str
    capacity: int


class RoomCreate(RoomBase):
    pass


class RoomResponse(RoomBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True