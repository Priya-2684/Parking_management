from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.slot_schema import SlotCreate, SlotResponse
from app.services import slot_service
from app.utils.dependencies import get_db, get_current_user
from app.utils.role_checker import get_current_admin

router = APIRouter(prefix="/slots", tags=["Slots"])

@router.post("/", response_model=SlotResponse)
def create_slot(data: SlotCreate, db: Session = Depends(get_db), admin = Depends(get_current_admin)):
    return slot_service.create_new_slot(db, data.slot_number, data.slot_type)

@router.get("/", response_model=List[SlotResponse])
def get_slots(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return slot_service.get_all_slots(db)