from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from ..database.MySQL import get_db
from ..crud import crud_option
from ..schemas.option import CreateOption

router = APIRouter(
    prefix="/option",
    tags=["Option"],
    responses={404: {"description": "Not found"}}
)

#Lấy option với vote_id truyền vào
@router.get("/")
def get_option_by_vote_id(vote_id: int, db: Session = Depends(get_db)):
    options = crud_option.get_option_by_vote_id(db, vote_id)
    if len(options)>0:
        return {"data": options}
    else:
        raise HTTPException(status_code=404, detail="User not found")

#Tạo option
@router.post("/")
def create_option(request: CreateOption, db: Session = Depends(get_db)):
    return crud_option.create_option(db, request)
