from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.models.user_model import User
from app.models.slot_model import Slot
from app.models.vehicle_model import Vehicle
from app.models.pricing_model import Pricing
from app.models.parking_record_model import ParkingRecord

from app.routes.auth_routes import router as auth_router
from app.routes.user_routes import router as user_router
from app.routes.slot_routes import router as slot_router
from app.routes.vehicle_routes import router as vehicle_router
from app.routes.pricing_routes import router as pricing_router
from app.routes.parking_routes import router as parking_router
from app.routes.dashboard_route import router as dashboard_router
Base.metadata.create_all(bind=engine)

app = FastAPI(title="INDIUM Parking Management System")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth_router)
app.include_router(user_router)
app.include_router(slot_router)
app.include_router(vehicle_router)
app.include_router(pricing_router)
app.include_router(parking_router)
app.include_router(dashboard_router)

@app.get("/")
def home():
    return {"message": "INDIUM Parking Management Backend Running"}