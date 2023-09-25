from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from typing import List

from ..database.MySQL import get_db
from ..crud import crud_vote
from ..schemas.vote import UpdaeContextVote, UpdateStatusVote, CreateVote

router = APIRouter(
    prefix="/vote",
    tags=["votes"],
    responses={404: {"description": "Not found"}}
)

@router.get("/")
def get_all_vote(db: Session = Depends(get_db)):
    votes = crud_vote.get_all_votes(db)
    if len(votes)>0:
        return {"data": votes}
    else:
        raise HTTPException(status_code=404, detail="User not found")
    
@router.get("/{id}")
def get_vote_by_id(id: int, db: Session = Depends(get_db)):
    vote = crud_vote.get_vote_by_id(db,id)
    if vote != None:
        return {"data": vote}
    else:
        raise HTTPException(status_code=404, detail=f"Vote with id {id} not found")
    
@router.put("/update_status")
def update_status_vote(id: int, request: UpdateStatusVote, db: Session = Depends(get_db)):
    return crud_vote.update_status_vote(db, id, request)

@router.put("/update_context")
def update_context_vote(id: int, request: UpdaeContextVote, db: Session = Depends(get_db)):
    return crud_vote.update_context_vote(db, id, request)

@router.post("/")
def create_vote(request: CreateVote, db: Session = Depends(get_db)):
    return crud_vote.create_vote(db, request)

@router.get("/result/{id}")
def get_result(id: int, type:str, db: Session = Depends(get_db)):
    if type in ["one_select", "many_select"]:
        option_ids, result = crud_vote.get_result_select(db,id)
        total_voted = 0
        result_list = []
        for option_id, total_user in result:
            result_list.append({"option_id": option_id, "total_user": total_user})
            option_ids.remove(option_id)
            total_voted+=total_user
        
        for option_id in option_ids:
            result_list.append({"option_id": option_id, "total_user": 0})
        return {"total_voted": total_voted, "data": result_list}
    
    elif type == "one_boolean":
        result = crud_vote.get_result_one_boolean(db, id)
        total_voted = 0
        result_dict = {}
        for boolean, total_user in result:
            result_dict[str(boolean)] =  total_user
            total_voted+=total_user
        return {"total_voted": total_voted, "data": result_dict}
    
    elif type =="many_boolean":
        result = crud_vote.get_result_many_boolean(db, id)
        total_voted = 0
        result_list = []
        for option_id, detail in result:
            detail_option = {}
            detail_option["option_id"] = option_id
            for boolean, total_user in detail:
                detail_option[str(boolean)] =  total_user
                total_voted+=total_user
            result_list.append(detail_option)
        return {"total_voted": total_voted, "data": result_list}
    
    else:
        raise HTTPException(status_code=404, detail=f"Vote don't have type {type}")
    
@router.get("/user_vote/{id}")
def get_user_vote(id: int, type:str, db: Session = Depends(get_db)):
    if type in ["one_select", "many_select"]:
        result = crud_vote.get_user_vote_select(db, id)
        data = []
        for option_id, users in result:
            user_list = []
            for user in users:
                user_list.append({"user_id": user.user_id,
                                "name": user.name,
                                "phone": user.phone,
                                "email": user.email})
            data.append({"option_id": option_id, "user": user_list})
        return {"data": data}
    
    elif type == "one_boolean":
        result = crud_vote.get_user_one_boolean(db, id)
        data = []
        user_true_list = []
        user_false_list = []
        for user, answer in result:
            if answer == "true":
                user_true_list.append({"user_id": user.user_id,
                                "name": user.name,
                                "phone": user.phone,
                                "email": user.email})
            else:
                user_false_list.append({"user_id": user.user_id,
                                "name": user.name,
                                "phone": user.phone,
                                "email": user.email})
        data.append({"answer": "true", "user": user_true_list})
        data.append({"answer": "false", "user": user_false_list})
        return {"data": data}
    
    elif type=="many_boolean":
        result = crud_vote.get_user_many_boolean(db, id)
        data = []
        for option_id, users in result:
            answer_list = []
            user_true_list = []
            user_false_list = []
            for user, answer in users:
                if answer == "true":
                    user_true_list.append({"user_id": user.user_id,
                                "name": user.name,
                                "phone": user.phone,
                                "email": user.email})
                else:
                    user_false_list.append({"user_id": user.user_id,
                                "name": user.name,
                                "phone": user.phone,
                                "email": user.email})
            answer_list.append({"answer": "true", "user": user_true_list})
            answer_list.append({"answer": "false", "user": user_false_list})
            data.append({"option_id": option_id, "answer": answer_list})
        return {"data": data}
    
    else:
        raise HTTPException(status_code=404, detail=f"Vote don't have type {type}")
    

