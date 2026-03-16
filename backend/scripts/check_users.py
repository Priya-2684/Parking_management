from app.database import SessionLocal
from app.repositories.user_repository import get_all_users

db = SessionLocal()
users = get_all_users(db)
print("Users in database:")
for user in users:
    print(f"Username: {user.username}, Email: {user.email}, Role: {user.role}")
db.close()
