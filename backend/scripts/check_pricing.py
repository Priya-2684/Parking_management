from app.database import SessionLocal
from app.models.pricing_model import Pricing

db = SessionLocal()
pricing = db.query(Pricing).all()
print("💰 Current Pricing:")
for p in pricing:
    print(f"   {p.vehicle_type}: ₹{p.price_per_hour}/hour")

db.close()
