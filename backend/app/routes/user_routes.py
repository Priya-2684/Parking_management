from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.user_model import User
from app.schemas.create_staff_schema import CreateStaffSchema
from app.utils.dependencies import get_current_user
from app.utils.role_checker import get_current_admin
from app.utils.password_handler import hash_password
from app.services import user_service

router = APIRouter(prefix="/users", tags=["Users"])

@router.get("/me")
def get_me(current_user=Depends(get_current_user)):
    return user_service.get_current_user_profile(current_user)

@router.get("/")
def get_users(db: Session = Depends(get_db), admin=Depends(get_current_admin)):
    return user_service.get_all_users(db)

@router.post("/create-staff")
def create_staff(
    data: CreateStaffSchema,
    db: Session = Depends(get_db),
    admin=Depends(get_current_admin)
):
    try:
        existing_user = db.query(User).filter(User.username == data.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already exists")

        existing_email = db.query(User).filter(User.email == data.email).first()
        if existing_email:
            raise HTTPException(status_code=400, detail="Email already exists")

        new_staff = User(
            username=data.username,
            email=data.email,
            password=hash_password(data.password),
            role="staff"
        )

        db.add(new_staff)
        db.commit()
        db.refresh(new_staff)

        return {
            "message": "Staff created successfully",
            "username": new_staff.username,
            "email": new_staff.email,
            "role": new_staff.role
        }

    except HTTPException:
        raise
    except Exception as e:
        db.rollback()
        print("CREATE STAFF ERROR:", str(e))
        raise HTTPException(status_code=500, detail=str(e))