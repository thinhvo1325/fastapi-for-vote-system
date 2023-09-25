from typing import List
from sqlalchemy.orm import Session
from ..models.result_select import ResultSelect
from ..schemas.result_select import CreateResultSelect, UpdateResultSelect
from fastapi import HTTPException
from fastapi.responses import JSONResponse

def get_user_select_option(db: Session, option_id: int):
    return db.query(ResultSelect).filter(ResultSelect.option_id == option_id).all()

def create_result_select(db: Session, request: CreateResultSelect):
    new_result_select = ResultSelect(
        user_id = request.user_id,
        option_id = request.option_id,
    )
    db.add(new_result_select)
    db.commit()
    db.refresh(new_result_select) 
    return new_result_select

#-----CRUD cho vote với kiểu bầu chọn 1 trong nhiều-----

#update lại bình chọn của user
def update_result_user(db: Session, option_id: int, user_id: int, request: UpdateResultSelect):
    result = db.query(ResultSelect).filter(ResultSelect.option_id == option_id,
                                         ResultSelect.user_id == user_id)
    if result.first() == None:
        raise HTTPException(status_code = 404, detail = f"Result was not found")
    else:
        result.update(request.dict())
        db.commit()
        return JSONResponse(
            content = {"detail": f"Result update successful"},
            status_code = 200
        )
