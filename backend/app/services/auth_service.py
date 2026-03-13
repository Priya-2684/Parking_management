from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.repositories import user_repository
from app.utils.password_handler import hash_password, verify_password
from app.utils.jwt_handler import create_access_token

def register_user(db: Session, username: str, email: str, password: str, role: str):
    existing_username = user_repository.get_user_by_username(db, username)
    if existing_username:
        raise HTTPException(status_code=400, detail="Username already exists")

    existing_email = user_repository.get_user_by_email(db, email)
    if existing_email:
        raise HTTPException(status_code=400, detail="Email already exists")

    hashed_password = hash_password(password)
    return user_repository.create_user(db, username, email, hashed_password, role)

def login_user(db: Session, username: str, password: str):
    user = user_repository.get_user_by_username(db, username)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")

    if not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Invalid username or password")

    token = create_access_token({"sub": user.username, "role": user.role})
    return {"access_token": token, "token_type": "bearer"}