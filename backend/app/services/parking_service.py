from datetime import datetime
import math
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import slot_repository, parking_repository
from app.services.vehicle_service import get_or_create_vehicle
from app.services.pricing_service import get_pricing_for_vehicle_type

def enter_vehicle(db: Session, vehicle_number: str, vehicle_type: str):
    active_record = parking_repository.get_active_record_by_vehicle_number(db, vehicle_number)
    if active_record:
        raise HTTPException(status_code=400, detail="Vehicle is already parked")

    slot = slot_repository.get_available_slot_by_type(db, vehicle_type)
    if not slot:
        raise HTTPException(status_code=404, detail="No available slot")

    get_or_create_vehicle(db, vehicle_number, vehicle_type)

    entry_time = datetime.utcnow()
    record = parking_repository.create_parking_record(
        db,
        vehicle_number=vehicle_number,
        vehicle_type=vehicle_type,
        slot_number=slot.slot_number,
        entry_time=entry_time
    )

    slot_repository.update_slot_status(db, slot, "Occupied")
    return record

def exit_vehicle(db: Session, vehicle_number: str):
    record = parking_repository.get_active_record_by_vehicle_number(db, vehicle_number)
    if not record:
        raise HTTPException(status_code=404, detail="Active parking record not found")

    pricing = get_pricing_for_vehicle_type(db, record.vehicle_type)

    exit_time = datetime.utcnow()
    duration = (exit_time - record.entry_time).total_seconds() / 3600
    duration = math.ceil(duration)
    charge = duration * pricing.price_per_hour

    updated_record = parking_repository.update_exit_details(
        db,
        record,
        exit_time=exit_time,
        duration_hours=duration,
        charge=charge
    )

    slot = slot_repository.get_slot_by_number(db, record.slot_number)
    if slot:
        slot_repository.update_slot_status(db, slot, "Available")

    return {
        "message": "Vehicle exited successfully",
        "vehicle_number": updated_record.vehicle_number,
        "slot_number": updated_record.slot_number,
        "duration_hours": updated_record.duration_hours,
        "charge": updated_record.charge
    }

def get_active_parkings(db: Session):
    return parking_repository.get_active_parking_records(db)

def get_parking_history(db: Session):
    return parking_repository.get_all_parking_records(db)