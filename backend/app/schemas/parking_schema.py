from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
import re

class EntryRequest(BaseModel):
    vehicle_number: str
    vehicle_type: str

    @validator('vehicle_number')
    def validate_vehicle_number(cls, v):
        if not v:
            raise ValueError('Vehicle number is required')
        
        # Remove spaces and convert to uppercase
        clean_number = v.replace(' ', '').upper()
        
        # Indian vehicle number pattern: AB12CD3456
        pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'
        
        if not re.match(pattern, clean_number):
            raise ValueError('Invalid vehicle number format. Use format: AB12CD3456 (e.g., MH12AB1234)')
        
        return clean_number

class ExitRequest(BaseModel):
    vehicle_number: str

    @validator('vehicle_number')
    def validate_vehicle_number(cls, v):
        if not v:
            raise ValueError('Vehicle number is required')
        
        # Remove spaces and convert to uppercase
        clean_number = v.replace(' ', '').upper()
        
        # Indian vehicle number pattern: AB12CD3456
        pattern = r'^[A-Z]{2}\d{2}[A-Z]{2}\d{4}$'
        
        if not re.match(pattern, clean_number):
            raise ValueError('Invalid vehicle number format. Use format: AB12CD3456 (e.g., MH12AB1234)')
        
        return clean_number

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

class EntryResponse(BaseModel):
    message: str
    vehicle_number: str
    vehicle_type: str
    slot_number: str
    entry_time: datetime

    class Config:
        from_attributes = True

class ExitResponse(BaseModel):
    message: str
    vehicle_number: str
    slot_number: str
    duration_hours: float
    charge: float
    entry_time: datetime
    exit_time: datetime

    class Config:
        from_attributes = True  # Your backend returns database objects, not dictionaries.
                                #This line allows FastAPI to convert those objects into API response JSON.