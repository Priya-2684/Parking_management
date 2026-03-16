import sys
sys.path.append('.')

# Test the exact same flow as the API but without HTTP
from app.database import SessionLocal
from app.schemas.parking_schema import EntryRequest
from app.services import parking_service

def test_direct_entry():
    """Test entry directly without HTTP layer"""
    db = SessionLocal()
    
    try:
        print("🧪 Testing Direct Vehicle Entry...")
        
        # Create the same data as API
        entry_data = EntryRequest(
            vehicle_number="MH12AB2222",
            vehicle_type="Bike"
        )
        
        print(f"🚗 Entering: {entry_data.vehicle_number} ({entry_data.vehicle_type})")
        
        # Call the service directly
        record = parking_service.enter_vehicle(db, entry_data.vehicle_number, entry_data.vehicle_type)
        
        print(f"✅ Success! Record created:")
        print(f"   Vehicle: {record.vehicle_number}")
        print(f"   Slot: {record.slot_number}")
        print(f"   Entry Time: {record.entry_time}")
        print(f"   Status: {record.status}")
        
        # Test the response construction that the API would do
        response = {
            "message": f"Vehicle entered successfully. Slot assigned: {record.slot_number}",
            "vehicle_number": record.vehicle_number,
            "vehicle_type": record.vehicle_type,
            "slot_number": record.slot_number,
            "entry_time": record.entry_time
        }
        
        print(f"✅ API Response would be: {response}")
        
    except Exception as e:
        print(f"❌ Direct entry failed: {e}")
        import traceback
        traceback.print_exc()
        
    finally:
        db.close()

if __name__ == "__main__":
    test_direct_entry()
