from pydantic import BaseModel

class PricingCreate(BaseModel):
    vehicle_type: str
    price_per_hour: float

class PricingResponse(BaseModel):
    id: int
    vehicle_type: str
    price_per_hour: float

    class Config:
        from_attributes = True