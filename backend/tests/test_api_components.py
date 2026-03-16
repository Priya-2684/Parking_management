import sys
sys.path.append('.')

# Test each step of the API call individually
from app.database import SessionLocal
from app.utils.dependencies import get_current_user
from app.schemas.parking_schema import EntryRequest
from app.services import parking_service

def test_api_components():
    """Test each component of the API call"""
    print("🧪 Testing API Components Step by Step...")
    print("=" * 50)
    
    # Step 1: Test database connection
    try:
        db = SessionLocal()
        print("✅ Database connection successful")
    except Exception as e:
        print(f"❌ Database connection failed: {e}")
        return
    
    # Step 2: Test user authentication (mock)
    try:
        # Mock current user - this might be the issue
        from app.models.user_model import User
        mock_user = User(id=1, username="admin", role="admin")
        print("✅ Mock user created")
    except Exception as e:
        print(f"❌ Mock user creation failed: {e}")
        return
    
    # Step 3: Test request validation
    try:
        entry_data = EntryRequest(
            vehicle_number="MH12AB3333",
            vehicle_type="Bike"
        )
        print(f"✅ Request validation successful: {entry_data}")
    except Exception as e:
        print(f"❌ Request validation failed: {e}")
        return
    
    # Step 4: Test service call
    try:
        record = parking_service.enter_vehicle(db, entry_data.vehicle_number, entry_data.vehicle_type)
        print(f"✅ Service call successful: {record.vehicle_number} in {record.slot_number}")
    except Exception as e:
        print(f"❌ Service call failed: {e}")
        import traceback
        traceback.print_exc()
        return
    
    # Step 5: Test response construction
    try:
        response = {
            "message": f"Vehicle entered successfully. Slot assigned: {record.slot_number}",
            "vehicle_number": record.vehicle_number,
            "vehicle_type": record.vehicle_type,
            "slot_number": record.slot_number,
            "entry_time": record.entry_time.isoformat() if record.entry_time else None
        }
        print(f"✅ Response construction successful: {response}")
    except Exception as e:
        print(f"❌ Response construction failed: {e}")
        return
    
    print("🎯 All API components working individually!")
    db.close()

if __name__ == "__main__":
    test_api_components()
