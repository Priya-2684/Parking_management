from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.pricing_schema import PricingCreate, PricingResponse
from app.services import pricing_service
from app.utils.dependencies import get_db, get_current_user
from app.utils.role_checker import get_current_admin

router = APIRouter(prefix="/pricing", tags=["Pricing"])

@router.post("/", response_model=PricingResponse)
def create_or_update_pricing(
    data: PricingCreate,
    db: Session = Depends(get_db),
    admin = Depends(get_current_admin)
):
    return pricing_service.create_or_update_pricing(db, data.vehicle_type, data.price_per_hour)

@router.get("/", response_model=List[PricingResponse])
def get_pricing(db: Session = Depends(get_db), current_user = Depends(get_current_user)):
    return pricing_service.get_all_pricing(db)