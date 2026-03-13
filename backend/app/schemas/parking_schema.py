from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class EntryRequest(BaseModel):
    vehicle_number: str
    vehicle_type: str

class ExitRequest(BaseModel):
    vehicle_number: str

class ParkingRecordResponse(BaseModel):
    id: int
    vehicle_number: str
    vehicle_type: str
    slot_number: str
    entry_time: datetime
    exit_time: Optional[datetime]
    duration_hours: Optional[float]
    charge: Optional[float]
    status: str

    class Config:
        from_attributes = True