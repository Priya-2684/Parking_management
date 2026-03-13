from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.repositories import slot_repository

def create_new_slot(db: Session, slot_number: str, slot_type: str):
    existing = slot_repository.get_slot_by_number(db, slot_number)
    if existing:
        raise HTTPException(status_code=400, detail="Slot already exists")

    return slot_repository.create_slot(db, slot_number, slot_type)

def get_all_slots(db: Session):
    return slot_repository.get_all_slots(db)