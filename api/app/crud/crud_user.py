from typing import List
from sqlalchemy.orm import Session
from ..models.user import User
from ..schemas.user import CreateUser

#Lấy thông tin tất cả user
def get_all_users(db: Session):
    return db.query(User).all()

#Lấy thông tin user với user_id
def get_user_by_id(db: Session, id: int):
    return db.query(User).filter(User.user_id == id).first()

#Tạo một user
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