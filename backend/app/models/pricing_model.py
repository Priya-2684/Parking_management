from sqlalchemy import Column, Integer, String, Float
from app.database import Base

class Pricing(Base):
    __tablename__ = "pricing"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_type = Column(String, unique=True, nullable=False)
    price_per_hour = Column(Float, nullable=False)