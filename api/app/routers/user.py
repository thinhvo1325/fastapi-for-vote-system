from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from typing import List

from ..database.MySQL import get_db
from ..crud import crud_user
from ..schemas.user import CreateUser

router = APIRouter(
    prefix="/user",
    tags=["users"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_all_user(db: Session = Depends(get_db)):
    users = crud_user.get_all_users(db)
    if len(users)>0:
        return {"data": users}
    else:
        raise HTTPException(status_code=404, detail="User not found")

@router.get("/{id}")
def get_user_by_id(id: int, db: Session = Depends(get_db)):
    user = crud_user.get_user_by_id(db,id)
    if user != None:
        return {"data": user}
    else:
        raise HTTPException(status_code=404, detail=f"User with id {id} not found")
    
@router.post("/")
def create_user(request: CreateUser, db: Session = Depends(get_db)):
    db_user = crud_user.get_user_by_email(db, request.email)
    if db_user != None:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud_user.create_user(db, request)


