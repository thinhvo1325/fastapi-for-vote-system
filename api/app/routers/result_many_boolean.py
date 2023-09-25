from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from ..database.MySQL import get_db
from ..crud import crud_result_many_boolean
from ..schemas.result_many_boolean import CreateResultManyBoolean, UpdateResultManyBoolean

router = APIRouter(
    prefix="/result_many_boolean",
    tags=["Result Many Boolean"],
    responses={404: {"description": "Not found"}}
)

#Lấy dữ liệu các user trả lời cho option đó với option_id truyền vào
@router.get("/")
def get_user_answer(option_id: int, db: Session = Depends(get_db)):
    answer = crud_result_many_boolean.get_user_answer(db, option_id)
    if len(answer)>0:
        return {"data": answer}
    else:
        raise HTTPException(status_code=404, detail="User not found")

#Tạo 1 dòng trong bảng result_many_boolean
@router.post("/")
def create_result_many_boolean(request: CreateResultManyBoolean, db: Session = Depends(get_db)):
    return crud_result_many_boolean.create_result_many_boolean(db, request)

#update lại câu trả lời của user
@router.put("/update")
def update_result_many_boolean(option_id: int, user_id: int, request: UpdateResultManyBoolean, db: Session = Depends(get_db)):
    return crud_result_many_boolean.update_result_many_boolean(db, option_id, user_id, request)