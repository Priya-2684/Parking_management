from fastapi import Depends, HTTPException
from app.utils.dependencies import get_current_user

def get_current_admin(current_user = Depends(get_current_user)):
    if not current_user or not current_user.role:
        raise HTTPException(status_code=403, detail="Admin only")

    if current_user.role.lower() != "admin":
        raise HTTPException(status_code=403, detail="Admin only")

    return current_user