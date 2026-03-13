from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import date

from app.models.slot_model import Slot
from app.models.parking_record_model import ParkingRecord

def get_dashboard_stats(db: Session):
    today = date.today()

    total_slots = db.query(Slot).count()

    occupied_slots = db.query(Slot).filter(
        Slot.status.ilike("occupied")
    ).count()

    available_slots = db.query(Slot).filter(
        Slot.status.ilike("available")
    ).count()

    today_entries = db.query(ParkingRecord).filter(
        func.date(ParkingRecord.entry_time) == today
    ).count()

    today_exits = db.query(ParkingRecord).filter(
        ParkingRecord.exit_time.isnot(None),
        func.date(ParkingRecord.exit_time) == today
    ).count()

    active_vehicles = db.query(ParkingRecord).filter(
        ParkingRecord.exit_time.is_(None)
    ).count()

    return {
        "total_slots": total_slots,
        "occupied_slots": occupied_slots,
        "available_slots": available_slots,
        "today_entries": today_entries,
        "today_exits": today_exits,
        "active_vehicles": active_vehicles,
    }