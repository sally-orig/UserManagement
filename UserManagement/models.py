from sqlalchemy import Column, Integer, Date, String
from .db import Base

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100), unique=True, nullable=False)
    age = Column(Integer, nullable=False)
    date_of_birth = Column(Date, nullable=False)

    class Config:
        orm_mode = True