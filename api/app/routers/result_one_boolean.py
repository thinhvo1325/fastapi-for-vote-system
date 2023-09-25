from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from ..database.MySQL import get_db
from ..crud import crud_result_one_boolean
from ..schemas.result_one_boolean import CreateResultOneBoolean, UpdateResultOneBoolean

router = APIRouter(
    prefix="/result_one_boolean",
    tags=["Result One Boolean"],
    responses={404: {"description": "Not found"}}
)

#Lấy dữ liệu các user trả lời cho option đó với option_id truyền vào
@router.get("/")
def get_user_answer(vote_id: int, db: Session = Depends(get_db)):
    answer = crud_result_one_boolean.get_user_answer(db, vote_id)
    if len(answer)>0:
        return {"data": answer}
    else:
        raise HTTPException(status_code=404, detail="User not found")

#Tạo 1 dòng trong bảng result_one_boolean
@router.post("/")
def create_result_one_boolean(request: CreateResultOneBoolean, db: Session = Depends(get_db)):
    return crud_result_one_boolean.create_result_one_boolean(db, request)

#update lại câu trả lời của user
@router.put("/update")
def update_result_one_boolean(vote_id: int, user_id: int, request: UpdateResultOneBoolean, db: Session = Depends(get_db)):
    return crud_result_one_boolean.update_result_one_boolean(db, vote_id, user_id, request)