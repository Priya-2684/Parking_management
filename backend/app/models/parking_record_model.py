from sqlalchemy import Column, Integer, String, Float, DateTime
from app.database import Base
from datetime import datetime

class ParkingRecord(Base):
    __tablename__ = "parking_records"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_number = Column(String, nullable=False, index=True)
    vehicle_type = Column(String, nullable=False)
    slot_number = Column(String, nullable=False)
    entry_time = Column(DateTime, default=datetime.utcnow)
    exit_time = Column(DateTime, nullable=True)
    duration_hours = Column(Float, nullable=True)
    charge = Column(Float, nullable=True)
    status = Column(String, default="Parked")  # Parked / Exited