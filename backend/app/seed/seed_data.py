from app.database import SessionLocal
from app.repositories import user_repository, slot_repository, pricing_repository
from app.utils.password_handler import hash_password

def seed():
    db = SessionLocal()

    admin = user_repository.get_user_by_username(db, "admin")
    if not admin:
        user_repository.create_user(
            db,
            username="admin",
            email="admin@gmail.com",
            password=hash_password("admin123"),
            role="admin"
        )

    # Create Bike Slots (B1-B20)
    for i in range(1, 21):
        slot_number = f"B{i}"
        if not slot_repository.get_slot_by_number(db, slot_number):
            slot_repository.create_slot(db, slot_number, "Bike")

    # Create Car Slots (C1-C15)
    for i in range(1, 16):
        slot_number = f"C{i}"
        if not slot_repository.get_slot_by_number(db, slot_number):
            slot_repository.create_slot(db, slot_number, "Car")

    # Create pricing for both vehicle types
    bike_pricing = pricing_repository.get_pricing_by_vehicle_type(db, "Bike")
    if not bike_pricing:
        pricing_repository.create_pricing(db, "Bike", 10)

    car_pricing = pricing_repository.get_pricing_by_vehicle_type(db, "Car")
    if not car_pricing:
        pricing_repository.create_pricing(db, "Car", 20)

    db.close()

if __name__ == "__main__":
    seed()