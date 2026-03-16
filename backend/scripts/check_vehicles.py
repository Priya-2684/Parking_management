import sys
sys.path.append('.')

from app.database import SessionLocal
from app.models.parking_record_model import ParkingRecord
from app.models.vehicle_model import Vehicle

# Check if there are any vehicles at all
db = SessionLocal()
vehicles = db.query(Vehicle).all()
print(f"🚗 Total Vehicles in Database: {len(vehicles)}")
for vehicle in vehicles:
    print(f"   {vehicle.vehicle_number} - {vehicle.vehicle_type}")

# Check if there are any parking records (active or completed)
parking_records = db.query(ParkingRecord).all()
print(f"\n📋 Total Parking Records: {len(parking_records)}")
for record in parking_records:
    print(f"   {record.vehicle_number} - Slot {record.slot_number} - Status: {record.status} - Entry: {record.entry_time}")

db.close()
