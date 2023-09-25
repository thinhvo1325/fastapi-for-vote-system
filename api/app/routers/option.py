from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from ..database.MySQL import get_db
from ..crud import crud_option
from ..schemas.option import CreateOption

router = APIRouter(
    prefix="/option",
    tags=["options"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_option_by_vote_id(vote_id: int, db: Session = Depends(get_db)):
    options = crud_option.get_option_by_vote_id(db, vote_id)
    if len(options)>0:
        return {"data": options}
    else:
        raise HTTPException(status_code=404, detail="User not found")


@router.post("/")
def create_option(request: CreateOption, db: Session = Depends(get_db)):
    return crud_option.create_option(db, request)
