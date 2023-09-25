from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session


from ..database.MySQL import get_db
from ..crud import crud_result_select
from ..schemas.result_select import CreateResultSelect, UpdateResultSelect

router = APIRouter(
    prefix="/result_select",
    tags=["Result Select"],
    responses={404: {"description": "Not found"}}
)

#Lấy dữ liệu các user bình chọn cho option đó với option_id truyền vào
@router.get("/")
def get_user_select_option(option_id: int, db: Session = Depends(get_db)):
    selects = crud_result_select.get_user_select_option(db, option_id)
    if len(selects)>0:
        return {"data": selects}
    else:
        raise HTTPException(status_code=404, detail="User not found")

#Tạo 1 dòng trong bảng result_select
@router.post("/")
def create_result_select(request: CreateResultSelect, db: Session = Depends(get_db)):
    return crud_result_select.create_result_select(db, request)

#update lại bình chọn của user
@router.put("/update")
def update_result_user(option_id: int, user_id: int, request: UpdateResultSelect, db: Session = Depends(get_db)):
    return crud_result_select.update_result_user(db, option_id, user_id, request)