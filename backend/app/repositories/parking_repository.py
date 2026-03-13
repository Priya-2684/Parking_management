from sqlalchemy.orm import Session
from app.models.parking_record_model import ParkingRecord

def create_parking_record(db: Session, vehicle_number: str, vehicle_type: str, slot_number: str, entry_time):
    record = ParkingRecord(
        vehicle_number=vehicle_number,
        vehicle_type=vehicle_type,
        slot_number=slot_number,
        entry_time=entry_time,
        status="Parked"
    )
    db.add(record)
    db.commit()
    db.refresh(record)
    return record

def get_active_record_by_vehicle_number(db: Session, vehicle_number: str):
    return db.query(ParkingRecord).filter(
        ParkingRecord.vehicle_number == vehicle_number,
        ParkingRecord.status == "Parked"
    ).first()

def update_exit_details(db: Session, record, exit_time, duration_hours: float, charge: float):
    record.exit_time = exit_time
    record.duration_hours = duration_hours
    record.charge = charge
    record.status = "Exited"
    db.commit()
    db.refresh(record)
    return record

def get_active_parking_records(db: Session):
    return db.query(ParkingRecord).filter(ParkingRecord.status == "Parked").all()

def get_all_parking_records(db: Session):
    return db.query(ParkingRecord).all()