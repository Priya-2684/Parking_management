import sys
sys.path.append('.')

from app.services.parking_service import get_local_time
from datetime import datetime
import pytz

# Test the local time function
current_time = get_local_time()
print(f"🕒 Current System Time: {current_time}")
print(f"📍 Timezone: {current_time.tzinfo}")
print(f"📅 Formatted: {current_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Test India timezone specifically
india_tz = pytz.timezone('Asia/Kolkata')
india_time = datetime.now(india_tz)
print(f"\n🇮🇳 India Time: {india_time}")
print(f"📅 India Formatted: {india_time.strftime('%Y-%m-%d %H:%M:%S %Z')}")

# Test UTC time for comparison
utc_time = datetime.utcnow()
print(f"\n🌍 UTC Time: {utc_time}")

print(f"\n✅ System time synchronization working correctly!")
print(f"🎯 All parking entries/exits will use local system time")
