from pydantic import BaseModel, EmailStr
from datetime import date

class UserBase(BaseModel):
    email: EmailStr
    age: int 
    date_of_birth: date 

class UserList(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class UserDetails(UserBase):
    id: int

    class Config:
        from_attributes = True