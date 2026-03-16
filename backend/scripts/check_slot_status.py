from app.database import SessionLocal
from app.models.slot_model import Slot

db = SessionLocal()
slots = db.query(Slot).all()
print("🔍 Current Slot Status Values:")
for slot in slots:
    print(f"   {slot.slot_number}: '{slot.status}'")

db.close()
