from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.services.dashboard_service import get_dashboard_stats
from app.schemas.dashboard_schema import DashboardStats

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

@router.get("/stats", response_model=DashboardStats)
def read_dashboard_stats(db: Session = Depends(get_db)):
    return get_dashboard_stats(db)