from sqlalchemy import Column, Integer, String
from app.database import Base

class Slot(Base):
    __tablename__ = "slots"

    id = Column(Integer, primary_key=True, index=True)
    slot_number = Column(String, unique=True, nullable=False, index=True)
    slot_type = Column(String, nullable=False)  # Bike / Car
    status = Column(String, nullable=False, default="Available")  # Available / Occupied