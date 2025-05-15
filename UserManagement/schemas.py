from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import date

class UserBase(BaseModel):
    email: EmailStr
    age: int 
    date_of_birth: date 

class UserList(BaseModel):
    id: int
    email: EmailStr

    model_config = ConfigDict(from_attributes=True)


class UserDetails(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)