from sqlalchemy.orm import Session
from .models import User
from .schemas import UserDetails

def format_response_for_pagination(data: dict, totalCount: int, limit: int, offset: int) -> dict:
    return {
        "totalCount": totalCount,
        "limit": limit,
        "offset": offset,
        "data": data
    }

def get_all_users(db: Session, limit: int, offset: int) -> dict:
    data = db.query(User).offset(offset).limit(limit).all()
    formatted_data = [
        {"id": user.id, "email": user.email} for user in data
    ]
    return format_response_for_pagination(
        data=formatted_data,
        totalCount=db.query(User).count(),
        limit=limit,
        offset=offset
    )

def get_user_by_id(db: Session, user_id: int) -> UserDetails:
    return db.query(User).filter(User.id == user_id).first()