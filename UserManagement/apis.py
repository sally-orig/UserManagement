from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .db import get_db
from .schemas import UserList, UserDetails
from .views import get_all_users, get_user_by_id

router = APIRouter()

# Get /users - list all users (id, email only)
@router.get("/", response_model=list[UserList], status_code=200)
async def get_users(db: Session = Depends(get_db)):
    users = get_all_users(db)
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

# Get /users/{user_id} - get user details by id
@router.get("/{user_id}", response_model=UserDetails, status_code=200)
async def get_user(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user