from pydantic import BaseModel, EmailStr

class CreateStaffSchema(BaseModel):
    username: str
    email: EmailStr
    password: str