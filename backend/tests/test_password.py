from app.database import SessionLocal
from app.repositories.user_repository import get_user_by_username
from app.utils.password_handler import verify_password

db = SessionLocal()
user = get_user_by_username(db, "admin")
if user:
    print(f"User found: {user.username}")
    print(f"Password verification with 'admin123': {verify_password('admin123', user.password)}")
    print(f"Password verification with 'admin': {verify_password('admin', user.password)}")
    print(f"Password verification with 'password': {verify_password('password', user.password)}")
else:
    print("Admin user not found!")
db.close()
