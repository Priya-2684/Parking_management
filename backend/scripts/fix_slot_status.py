from app.database import SessionLocal
from app.models.slot_model import Slot

db = SessionLocal()

# Fix the typo in slot status
slot_b1 = db.query(Slot).filter(Slot.slot_number == "B1").first()
if slot_b1:
    slot_b1.status = "Occupied"
    db.commit()
    print("✅ Fixed slot B1 status from 'Occupied' to 'Occupied'")

db.close()
