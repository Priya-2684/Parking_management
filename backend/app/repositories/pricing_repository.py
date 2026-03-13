from sqlalchemy.orm import Session
from app.models.pricing_model import Pricing

def get_pricing_by_vehicle_type(db: Session, vehicle_type: str):
    return db.query(Pricing).filter(Pricing.vehicle_type == vehicle_type).first()

def create_pricing(db: Session, vehicle_type: str, price_per_hour: float):
    pricing = Pricing(vehicle_type=vehicle_type, price_per_hour=price_per_hour)
    db.add(pricing)
    db.commit()
    db.refresh(pricing)
    return pricing

def update_pricing(db: Session, pricing, price_per_hour: float):
    pricing.price_per_hour = price_per_hour
    db.commit()
    db.refresh(pricing)
    return pricing

def get_all_pricing(db: Session):
    return db.query(Pricing).all()