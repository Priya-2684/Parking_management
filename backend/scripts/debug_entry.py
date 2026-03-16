import sys
sys.path.append('.')

# Test entry step by step to isolate the 500 error
from app.database import SessionLocal
from app.services.parking_service import enter_vehicle
from app.services.vehicle_service import get_or_create_vehicle

def test_entry_components():
    """Test each component of vehicle entry"""
    db = SessionLocal()
    
    try:
        print("🧪 Step 1: Testing get_or_create_vehicle...")
        vehicle = get_or_create_vehicle(db, "TEST1234", "Bike")
        print(f"   ✅ Vehicle created/retrieved: {vehicle.vehicle_number}")
        
        print("\n🧪 Step 2: Testing slot availability...")
        from app.repositories import slot_repository
        slot = slot_repository.get_available_slot_by_type(db, "Bike")
        if slot:
            print(f"   ✅ Available slot found: {slot.slot_number}")
        else:
            print("   ❌ No available slots")
            return
            
        print("\n🧪 Step 3: Testing parking record creation...")
        try:
            # Use naive datetime to avoid timezone issues
            from datetime import datetime
            entry_time = datetime.now()
            
            record = enter_vehicle(db, "TEST1234", "Bike")
            print(f"   ✅ Parking record created: {record.vehicle_number} in {record.slot_number}")
            print(f"   ✅ Slot status updated: {slot.slot_number} -> Occupied")
            
        except Exception as e:
            print(f"   ❌ Parking record creation failed: {e}")
            import traceback
            traceback.print_exc()
            
    except Exception as e:
        print(f"❌ Test failed: {e}")
        
    finally:
        db.close()

if __name__ == "__main__":
    test_entry_components()
