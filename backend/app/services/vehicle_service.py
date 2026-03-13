from sqlalchemy.orm import Session
from app.repositories import vehicle_repository

def get_or_create_vehicle(db: Session, vehicle_number: str, vehicle_type: str):
    vehicle = vehicle_repository.get_vehicle_by_number(db, vehicle_number)
    if vehicle:
        return vehicle

    return vehicle_repository.create_vehicle(db, vehicle_number, vehicle_type)

def get_all_vehicles(db: Session):
    return vehicle_repository.get_all_vehicles(db)