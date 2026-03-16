from app.database import SessionLocal
from app.repositories.slot_repository import get_all_slots

db = SessionLocal()
slots = get_all_slots(db)
print("🚦 Current Parking Slots:")
print("=" * 50)

bike_slots = [s for s in slots if s.slot_type == "Bike"]
car_slots = [s for s in slots if s.slot_type == "Car"]

print(f"🏍️  Bike Slots ({len(bike_slots)} total):")
for slot in bike_slots:
    status = "🟢 Available" if slot.status == "Available" else "🔴 Occupied"
    print(f"   {slot.slot_number}: {status}")

print(f"\n🚗 Car Slots ({len(car_slots)} total):")
for slot in car_slots:
    status = "🟢 Available" if slot.status == "Available" else "🔴 Occupied"
    print(f"   {slot.slot_number}: {status}")

print(f"\n📊 Total Slots: {len(slots)}")
print(f"🟢 Available: {len([s for s in slots if s.status == 'Available'])}")
print(f"🔴 Occupied: {len([s for s in slots if s.status == 'Occupied'])}")

db.close()
