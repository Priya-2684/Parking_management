import sys
sys.path.append('.')

from app.database import SessionLocal
from app.models.user_model import User
from app.models.parking_record_model import ParkingRecord

# Check current users and their roles
db = SessionLocal()
users = db.query(User).all()
print("👥 Current Users:")
for user in users:
    print(f"   {user.username} - {user.role}")

# Check active parking records
active_records = db.query(ParkingRecord).filter(ParkingRecord.status == "Active").all()
print(f"\n🚗 Active Parking Records: {len(active_records)}")
for record in active_records:
    print(f"   {record.vehicle_number} - Slot {record.slot_number} - {record.entry_time}")

db.close()
