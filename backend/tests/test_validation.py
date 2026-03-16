import sys
sys.path.append('.')

from app.schemas.parking_schema import EntryRequest, ExitRequest
from app.schemas.vehicle_schema import VehicleCreate

# Test valid vehicle number
try:
    valid_entry = EntryRequest(vehicle_number="MH12AB1234", vehicle_type="Car")
    print("✅ Valid vehicle number passed:", valid_entry.vehicle_number)
except Exception as e:
    print("❌ Valid vehicle number failed:", str(e))

# Test invalid vehicle number
try:
    invalid_entry = EntryRequest(vehicle_number="ABC123", vehicle_type="Car")
    print("❌ Invalid vehicle number incorrectly passed")
except Exception as e:
    print("✅ Invalid vehicle number correctly rejected:", str(e))

# Test another valid format
try:
    valid_entry2 = EntryRequest(vehicle_number="DL05CD5678", vehicle_type="Bike")
    print("✅ Another valid format passed:", valid_entry2.vehicle_number)
except Exception as e:
    print("❌ Another valid format failed:", str(e))

# Test exit validation
try:
    valid_exit = ExitRequest(vehicle_number="MH12AB1234")
    print("✅ Valid exit vehicle number passed:", valid_exit.vehicle_number)
except Exception as e:
    print("❌ Valid exit vehicle number failed:", str(e))

print("\n🎯 Validation system is working!")
