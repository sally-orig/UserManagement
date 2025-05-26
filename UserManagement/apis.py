from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import Any
from .db import get_db
from .schemas import UserDetails
from .views import get_all_users, get_user_by_id

router = APIRouter()

# Get /users - list all users (id, email only)
@router.get("", response_model=dict, status_code=200)
async def get_users(db: Session = Depends(get_db), limit: int = Query(20, ge=1), offset: int = Query(0, ge=0)):
    users = get_all_users(db, limit, offset)
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