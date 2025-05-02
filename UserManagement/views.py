from sqlalchemy.orm import Session
from .models import User
from .schemas import UserList, UserDetails

def get_all_users(db: Session) -> list[UserList]:
    return db.query(User).all()

def get_user_by_id(db: Session, user_id: int) -> UserDetails:
    return db.query(User).filter(User.id == user_id).first()