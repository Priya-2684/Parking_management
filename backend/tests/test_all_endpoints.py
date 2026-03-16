import requests
import json

base_url = "http://localhost:8000"

def test_api_endpoint(endpoint, data, description):
    """Test API endpoint and return results"""
    try:
        # Login as admin
        login_response = requests.post(f"{base_url}/auth/login", json={
            "username": "admin", 
            "password": "admin123"
        })
        
        if login_response.status_code == 200:
            token = login_response.json()["access_token"]
            headers = {"Authorization": f"Bearer {token}"}
            
            print(f"\n🧪 Testing {endpoint}...")
            response = requests.post(f"{base_url}{endpoint}", json=data, headers=headers)
            
            print(f"Status: {response.status_code}")
            if response.status_code == 200:
                print(f"✅ {description} - SUCCESS")
                print(f"Response: {json.dumps(response.json(), indent=2)}")
            else:
                print(f"❌ {description} - FAILED")
                print(f"Error: {response.text}")
        else:
            print(f"❌ Login failed for {endpoint}")
            
    except Exception as e:
        print(f"❌ Error testing {endpoint}: {e}")

# Test all major endpoints
print("🔍 API Endpoint Testing")
print("=" * 50)

# Test vehicle entry
test_api_endpoint("/parking/entry", {
    "vehicle_number": "MH12AB1234",
    "vehicle_type": "Bike"
}, "Vehicle Entry")

# Test vehicle exit with valid format
test_api_endpoint("/parking/exit", {
    "vehicle_number": "MH12AB1234"
}, "Vehicle Exit (Valid Format)")

# Test vehicle exit with invalid format
test_api_endpoint("/parking/exit", {
    "vehicle_number": "INVALID"
}, "Vehicle Exit (Invalid Format)")

# Test getting active parking
test_api_endpoint("/parking/active", {}, "Get Active Parking")

# Test getting parking history
test_api_endpoint("/parking/history", {}, "Get Parking History")

print("\n" + "=" * 50)
print("🎯 Test Complete!")
