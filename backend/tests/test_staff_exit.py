import requests
import json

# Test exit API with different scenarios
base_url = "http://localhost:8000"

# First, login as staff to get token
login_data = {
    "username": "testuser",
    "password": "test123"  # Assuming this is the password
}

try:
    print("🔑 Attempting staff login...")
    login_response = requests.post(f"{base_url}/auth/login", json=login_data)
    if login_response.status_code == 200:
        token = login_response.json()["access_token"]
        print(f"✅ Staff login successful")
        
        # Try to exit a vehicle that is actually parked
        headers = {"Authorization": f"Bearer {token}"}
        
        # Test with an actual parked vehicle that has proper format
        exit_data = {"vehicle_number": "MH12CF4567"}  # This vehicle is in Slot B3 and has proper format
        
        print(f"\n🚗 Attempting to exit vehicle 'MH12CF4567' as staff...")
        exit_response = requests.post(f"{base_url}/parking/exit", json=exit_data, headers=headers)
        
        print(f"Status Code: {exit_response.status_code}")
        print(f"Response: {exit_response.text}")
        
        # Also test with admin login for comparison
        print(f"\n🔑 Testing with admin login...")
        admin_login = {"username": "admin", "password": "admin123"}
        admin_response = requests.post(f"{base_url}/auth/login", json=admin_login)
        if admin_response.status_code == 200:
            admin_token = admin_response.json()["access_token"]
            admin_headers = {"Authorization": f"Bearer {admin_token}"}
            
            admin_exit_response = requests.post(f"{base_url}/parking/exit", json=exit_data, headers=admin_headers)
            print(f"Admin Exit Status Code: {admin_exit_response.status_code}")
            print(f"Admin Exit Response: {admin_exit_response.text}")
        
    else:
        print(f"❌ Staff login failed: {login_response.text}")
        
except Exception as e:
    print(f"❌ Error: {e}")
