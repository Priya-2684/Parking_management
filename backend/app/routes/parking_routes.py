from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.parking_schema import EntryRequest, ExitRequest, ParkingRecordResponse
from app.services import parking_service
from app.utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/parking", tags=["Parking"])

@router.post("/entry", response_model=ParkingRecordResponse)
def vehicle_entry(
    data: EntryRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return parking_service.enter_vehicle(db, data.vehicle_number, data.vehicle_type)

@router.post("/exit")
def vehicle_exit(
    data: ExitRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return parking_service.exit_vehicle(db, data.vehicle_number)

@router.get("/active", response_model=List[ParkingRecordResponse])
def active_parking(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return parking_service.get_active_parkings(db)

@router.get("/history", response_model=List[ParkingRecordResponse])
def parking_history(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return parking_service.get_parking_history(db)