from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.services import vehicle_service
from app.utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/vehicles", tags=["Vehicles"])

@router.get("/")
def get_vehicles(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return vehicle_service.get_all_vehicles(db)