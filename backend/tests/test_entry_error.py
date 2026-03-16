import requests

# Test entry with detailed error capture
base_url = "http://localhost:8000"

print("🧪 Testing Vehicle Entry with Error Details...")
print("=" * 50)

# Login as admin
login_response = requests.post(f"{base_url}/auth/login", json={
    "username": "admin", 
    "password": "admin123"
})

if login_response.status_code == 200:
    token = login_response.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}
    
    # Test vehicle entry (without auth for debugging)
    entry_data = {
        "vehicle_number": "MH12AB1111",
        "vehicle_type": "Bike"
    }
    
    print(f"🚗 Attempting entry: {entry_data['vehicle_number']} ({entry_data['vehicle_type']})")
    
    response = requests.post(f"{base_url}/parking/entry", json=entry_data)  # No headers
    
    print(f"Status Code: {response.status_code}")
    
    if response.status_code == 500:
        print("❌ 500 Error - Detailed Response:")
        print(response.text)
        
        # Try to parse the error
        try:
            error_json = response.json()
            if "detail" in error_json:
                print(f"Error Detail: {error_json['detail']}")
        except:
            print("Could not parse error JSON")
            
    elif response.status_code == 200:
        print("✅ Entry Successful!")
        print(response.json())
    else:
        print(f"❌ Unexpected error: {response.text}")
        
else:
    print(f"❌ Login failed: {login_response.text}")

print("=" * 50)
