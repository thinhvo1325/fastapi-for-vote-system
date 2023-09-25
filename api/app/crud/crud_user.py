from typing import List
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import CreateUser

def get_all_users(db: Session):
    return db.query(User).all()

def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.user_id == id).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def create_user(db: Session, request: CreateUser):
    new_user = User(
        name = request.name,
        email = request.email,
        phone = request.phone
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user