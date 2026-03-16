import requests

# Test the minimal endpoint
base_url = "http://localhost:8000"

print("🧪 Testing Minimal Endpoint...")
print("=" * 50)

entry_data = {
    "vehicle_number": "MH12AB1111",
    "vehicle_type": "Bike"
}

response = requests.post(f"{base_url}/parking/test-entry", json=entry_data)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")

print("=" * 50)
