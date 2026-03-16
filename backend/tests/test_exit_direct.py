import sys
sys.path.append('.')

from app.database import SessionLocal
from app.services.parking_service import exit_vehicle
from app.models.parking_record_model import ParkingRecord

# Test the exit function directly
db = SessionLocal()

try:
    print("🧪 Testing exit_vehicle function directly...")
    
    # Test with a known parked vehicle
    result = exit_vehicle(db, "MH12CD4567")
    print(f"✅ Exit successful: {result}")
    
except Exception as e:
    print(f"❌ Exit failed with error: {e}")
    import traceback
    traceback.print_exc()

finally:
    db.close()
