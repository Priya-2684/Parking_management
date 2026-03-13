from sqlalchemy.orm import Session
from app.models.slot_model import Slot

def create_slot(db: Session, slot_number: str, slot_type: str):
    slot = Slot(slot_number=slot_number, slot_type=slot_type, status="Available")
    db.add(slot)
    db.commit()
    db.refresh(slot)
    return slot

def get_all_slots(db: Session):
    return db.query(Slot).all()

def get_slot_by_number(db: Session, slot_number: str):
    return db.query(Slot).filter(Slot.slot_number == slot_number).first()

def get_available_slot_by_type(db: Session, slot_type: str):
    return db.query(Slot).filter(
        Slot.slot_type == slot_type,
        Slot.status == "Available"
    ).first()

def update_slot_status(db: Session, slot, status: str):
    slot.status = status
    db.commit()
    db.refresh(slot)
    return slot