from typing import List
from sqlalchemy.orm import Session
from ..models.result_one_boolean import ResultOneBoolean
from ..schemas.result_one_boolean import CreateResultOneBoolean, UpdateResultOneBoolean
from fastapi import HTTPException
from fastapi.responses import JSONResponse

#Lấy dữ liệu các user trả lời cho option đó với option_id truyền vào
def get_user_answer(db: Session, vote_id: int):
    return db.query(ResultOneBoolean).filter(ResultOneBoolean.vote_id == vote_id).all()

#Tạo 1 dòng trong bảng result_one_boolean
def create_result_one_boolean(db: Session, request: CreateResultOneBoolean):
    new_result_one_boolean = ResultOneBoolean(
        user_id = request.user_id,
        vote_id = request.vote_id,
        answer = request.answer
    )
    db.add(new_result_one_boolean)
    db.commit()
    db.refresh(new_result_one_boolean) 
    return new_result_one_boolean

#update lại câu trả lời của user
def update_result_one_boolean(db: Session, vote_id: int, user_id: int, request: UpdateResultOneBoolean):
    result = db.query(ResultOneBoolean).filter(ResultOneBoolean.vote_id == vote_id,
                                         ResultOneBoolean.user_id == user_id)
    if result.first() == None:
        raise HTTPException(status_code = 404, detail = f"Result was not found")
    else:
        result.update(request.dict())
        db.commit()
        return JSONResponse(
            content = {"detail": f"Result update successful"},
            status_code = 200
        )
