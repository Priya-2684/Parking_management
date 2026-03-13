from sqlalchemy.orm import Session
from app.models.vehicle_model import Vehicle

def get_vehicle_by_number(db: Session, vehicle_number: str):
    return db.query(Vehicle).filter(Vehicle.vehicle_number == vehicle_number).first()

def create_vehicle(db: Session, vehicle_number: str, vehicle_type: str):
    vehicle = Vehicle(vehicle_number=vehicle_number, vehicle_type=vehicle_type)
    db.add(vehicle)
    db.commit()
    db.refresh(vehicle)
    return vehicle

def get_all_vehicles(db: Session):
    return db.query(Vehicle).all()