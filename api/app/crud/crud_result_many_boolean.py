from typing import List
from sqlalchemy.orm import Session
from ..models.result_many_boolean import ResultManyBoolean
from ..schemas.result_many_boolean import CreateResultManyBoolean, UpdateResultManyBoolean
from fastapi import HTTPException
from fastapi.responses import JSONResponse

#Lấy dữ liệu các user trả lời cho option đó với option_id truyền vào
def get_user_answer(db: Session, option_id: int):
    return db.query(ResultManyBoolean).filter(ResultManyBoolean.option_id == option_id).all()

#Tạo 1 dòng trong bảng result_many_boolean
def create_result_many_boolean(db: Session, request: CreateResultManyBoolean):
    new_result_many_boolean = ResultManyBoolean(
        user_id = request.user_id,
        option_id = request.option_id,
        answer = request.answer
    )
    db.add(new_result_many_boolean)
    db.commit()
    db.refresh(new_result_many_boolean) 
    return new_result_many_boolean

#update lại câu trả lời của user
def update_result_many_boolean(db: Session, option_id: int, user_id: int, request: UpdateResultManyBoolean):
    result = db.query(ResultManyBoolean).filter(ResultManyBoolean.option_id == option_id,
                                         ResultManyBoolean.user_id == user_id)
    if result.first() == None:
        raise HTTPException(status_code = 404, detail = f"Result was not found")
    else:
        result.update(request.dict())
        db.commit()
        return JSONResponse(
            content = {"detail": f"Result update successful"},
            status_code = 200
        )
