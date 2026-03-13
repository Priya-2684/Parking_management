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

    if not slot_repository.get_slot_by_number(db, "B1"):
        slot_repository.create_slot(db, "B1", "Bike")

    if not slot_repository.get_slot_by_number(db, "B2"):
        slot_repository.create_slot(db, "B2", "Bike")

    if not slot_repository.get_slot_by_number(db, "B3"):
        slot_repository.create_slot(db, "B3", "Bike")

    bike_pricing = pricing_repository.get_pricing_by_vehicle_type(db, "Bike")
    if not bike_pricing:
        pricing_repository.create_pricing(db, "Bike", 10)

    db.close()

if __name__ == "__main__":
    seed()