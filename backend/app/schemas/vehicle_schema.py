from pydantic import BaseModel, validator
import re

class VehicleCreate(BaseModel):
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

class VehicleResponse(BaseModel):
    id: int
    vehicle_number: str
    vehicle_type: str

    class Config:
        from_attributes = True