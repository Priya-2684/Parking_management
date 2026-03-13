from pydantic import BaseModel

class SlotCreate(BaseModel):
    slot_number: str
    slot_type: str

class SlotResponse(BaseModel):
    id: int
    slot_number: str
    slot_type: str
    status: str

    class Config:
        from_attributes = True