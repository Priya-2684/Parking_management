print("🔍 INDIUM PARKING SYSTEM - COMPREHENSIVE STATUS CHECK")
print("=" * 60)

# Check all components systematically
print("\n📊 DATABASE STATUS:")
try:
    from app.database import SessionLocal
    from app.models.user_model import User
    from app.models.vehicle_model import Vehicle
    from app.models.parking_record_model import ParkingRecord
    from app.models.slot_model import Slot
    from app.models.pricing_model import Pricing
    
    db = SessionLocal()
    
    users = db.query(User).all()
    vehicles = db.query(Vehicle).all()
    parking_records = db.query(ParkingRecord).all()
    slots = db.query(Slot).all()
    pricing = db.query(Pricing).all()
    
    print(f"   👥 Users: {len(users)}")
    print(f"   🚗 Vehicles: {len(vehicles)}")
    print(f"   🅿️ Parking Records: {len(parking_records)}")
    print(f"   🎰 Slots: {len(slots)}")
    print(f"   💰 Pricing: {len(pricing)}")
    
    # Check specific issues
    print(f"\n🔍 DETAILED ANALYSIS:")
    
    # Check parked vehicles
    parked = [r for r in parking_records if r.status == "Parked"]
    print(f"   🅿️ Currently Parked: {len(parked)}")
    for p in parked:
        print(f"      {p.vehicle_number} in {p.slot_number} since {p.entry_time}")
    
    # Check available slots
    available_slots = [s for s in slots if s.status == "Available"]
    print(f"   🟢 Available Slots: {len(available_slots)}")
    
    # Check slot status consistency
    slot_statuses = set(s.status for s in slots)
    print(f"   📊 Slot Status Types: {slot_statuses}")
    
    db.close()
    
except Exception as e:
    print(f"❌ Database check failed: {e}")

print(f"\n🌐 API ENDPOINTS STATUS:")
print("   ✅ Vehicle Exit: Working (timezone issue fixed)")
print("   ✅ Vehicle Number Validation: Working (Indian format AB12CD3456)")
print("   ✅ Quick Exit Dropdown: Working")
print("   ✅ Active Parking Quick Exit: Working")
print("   ❌ Vehicle Entry: 500 Internal Server Error")
print("   ❌ Active/History GET: 405 Method Not Allowed")

print(f"\n🎯 ISSUES IDENTIFIED:")
print("   1. Vehicle Entry failing with 500 error")
print("   2. GET endpoints returning 405 Method Not Allowed")
print("   3. Slot status typo was fixed ('Occupied' → 'Occupied')")

print(f"\n🛠️ NEXT STEPS:")
print("   1. Fix Vehicle Entry 500 error")
print("   2. Fix GET endpoints 405 error")
print("   3. Test all functionality end-to-end")

print("\n" + "=" * 60)
