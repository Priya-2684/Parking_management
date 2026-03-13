from sqlalchemy.orm import Session
from app.repositories import user_repository

def get_current_user_profile(current_user):
    return current_user

def get_all_users(db: Session):
    return user_repository.get_all_users(db)