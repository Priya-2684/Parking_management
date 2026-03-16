from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.parking_schema import EntryRequest, ExitRequest, ParkingRecordResponse, EntryResponse, ExitResponse
from app.services import parking_service
from app.utils.dependencies import get_db, get_current_user

router = APIRouter(prefix="/parking", tags=["Parking"])

@router.post("/test-entry")
def test_entry(
    data: EntryRequest,
    db: Session = Depends(get_db)
):
    try:
        return {"status": "ok", "vehicle": data.vehicle_number, "type": data.vehicle_type}
    except Exception as e:
        return {"error": str(e)}

@router.post("/entry")
def vehicle_entry(
    data: EntryRequest,
    db: Session = Depends(get_db)
):
    try:
        # Call the service
        record = parking_service.enter_vehicle(db, data.vehicle_number, data.vehicle_type)
        
        # Return simple response without datetime serialization issues
        return {
            "message": f"Vehicle entered successfully. Slot assigned: {record.slot_number}",
            "vehicle_number": record.vehicle_number,
            "vehicle_type": record.vehicle_type,
            "slot_number": record.slot_number,
            "entry_time": str(record.entry_time)  # Convert to string
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        print(f"Vehicle entry error: {e}")
        raise HTTPException(status_code=500, detail=f"Internal server error: {str(e)}")

@router.post("/exit", response_model=ExitResponse)
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