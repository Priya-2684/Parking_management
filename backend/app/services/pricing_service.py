from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import pricing_repository

def create_or_update_pricing(db: Session, vehicle_type: str, price_per_hour: float):
    existing = pricing_repository.get_pricing_by_vehicle_type(db, vehicle_type)

    if existing:
        return pricing_repository.update_pricing(db, existing, price_per_hour)

    return pricing_repository.create_pricing(db, vehicle_type, price_per_hour)

def get_all_pricing(db: Session):
    return pricing_repository.get_all_pricing(db)

def get_pricing_for_vehicle_type(db: Session, vehicle_type: str):
    pricing = pricing_repository.get_pricing_by_vehicle_type(db, vehicle_type)
    if not pricing:
        raise HTTPException(status_code=404, detail="Pricing not found")
    return pricing