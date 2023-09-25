from typing import List
from sqlalchemy.orm import Session
from sqlalchemy import select
from ..models.vote import Vote
from ..models.user import User
from ..models.option import Option
from ..models.result_select import ResultSelect
from ..models.result_one_boolean import ResultOneBoolean
from ..models.result_many_boolean import ResultManyBoolean
from ..schemas.vote import UpdaeContextVote, UpdateStatusVote, CreateVote
from sqlalchemy import func
from fastapi import HTTPException
from fastapi.responses import JSONResponse

def get_all_votes(db: Session):
    return db.query(Vote).all()

def get_vote_by_id(db: Session, id: int):
    return db.query(Vote).filter(Vote.vote_id == id).first()

def update_status_vote(db: Session, id: int, request: UpdateStatusVote):
    vote = db.query(Vote).filter(Vote.vote_id == id)
    if vote.first() == None:
        raise HTTPException(status_code = 404, detail = f"Vote with id {id} is not found")
    else:
        if vote.first().status.value != 'completed':
            db.query(Vote).filter(Vote.vote_id == id).update(request.dict())
            db.commit()
            return JSONResponse(
                content = {"detail": f"Vote id {id} update status successful"},
                status_code = 200
            )
        else:
            return JSONResponse(
                content = {"detail": f"Vote id {id} update status failed"},
                status_code = 400
            )
        
def update_context_vote(db: Session, id: int, request: UpdaeContextVote):
    vote = db.query(Vote).filter(Vote.vote_id == id)
    if vote.first() == None:
        raise HTTPException(status_code = 404, detail = f"Vote with id {id} is not found")
    else:
        if vote.first().status.value == 'upcoming':
            db.query(Vote).filter(Vote.vote_id == id).update(request.dict())
            db.commit()
            return JSONResponse(
                content = {"detail": f"Vote id {id} update status successful"},
                status_code = 200
            )
        else:
            return JSONResponse(
                content = {"detail": f"Vote id {id} update status failed"},
                status_code = 400
            )
        
def create_vote(db: Session, request: CreateVote):
    new_vote = Vote(
        name = request.name,
        type = request.type,
        start_time = request.start_time,
        end_time = request.end_time,
        context = request.context,
        status = request.status,
        user_id = request.user_id
    )
    db.add(new_vote)
    db.commit()
    db.refresh(new_vote)
    return new_vote

def get_result_select(db: Session, id: int):
    vote = db.query(Vote).filter(Vote.vote_id == id)
    if vote.first() == None:
        raise HTTPException(status_code = 404, detail = f"Vote with id {id} is not found")
    else:
        options = db.query(Option).filter(Option.vote_id == id).all()
        option_ids = [option.option_id for option in options]

        statistic = db.query(ResultSelect.option_id, func.count(ResultSelect.user_id))\
                    .filter(ResultSelect.option_id.in_(option_ids))\
                    .group_by(ResultSelect.option_id).all()
        
        return option_ids, statistic
    

def get_result_one_boolean(db: Session, id: int):
    vote = db.query(Vote).filter(Vote.vote_id == id)
    if vote.first() == None:
        raise HTTPException(status_code = 404, detail = f"Vote with id {id} is not found")
    else:
        statistic = db.query(ResultOneBoolean.answer, func.count(ResultOneBoolean.answer))\
                    .filter(ResultOneBoolean.vote_id == id)\
                    .group_by(ResultOneBoolean.answer).all()
        return statistic
    
def get_result_many_boolean(db: Session, id: int):
    vote = db.query(Vote).filter(Vote.vote_id == id)
    if vote.first() == None:
        raise HTTPException(status_code = 404, detail = f"Vote with id {id} is not found")
    else:
        options = db.query(Option).filter(Option.vote_id == id).all()
        option_ids = [option.option_id for option in options]
        result = []
        for option_id in option_ids:
            query = db.query(ResultManyBoolean.answer, func.count(ResultManyBoolean.answer))\
                        .filter(ResultManyBoolean.option_id == option_id)\
                        .group_by(ResultManyBoolean.answer).all()
            result.append([option_id, query])
        return result
    

def get_user_vote_select(db: Session, id: int):
    vote = db.query(Vote).filter(Vote.vote_id == id)
    if vote.first() == None:
        raise HTTPException(status_code = 404, detail = f"Vote with id {id} is not found")
    else:
        options = db.query(Option).filter(Option.vote_id == id).all()
        option_ids = [option.option_id for option in options]
        list_user = []
        for option_id in option_ids:
            statistic = db.query(User).join(ResultSelect, ResultSelect.user_id == User.user_id)\
                        .filter(ResultSelect.option_id == option_id).all()
            list_user.append([option_id, statistic])
        return list_user
    
    
def get_user_one_boolean(db: Session, id: int):
    vote = db.query(Vote).filter(Vote.vote_id == id)
    if vote.first() == None:
        raise HTTPException(status_code = 404, detail = f"Vote with id {id} is not found")
    else:
        statistic = db.query(User, ResultOneBoolean.answer).join(ResultOneBoolean, ResultOneBoolean.user_id == User.user_id)\
                        .filter(ResultOneBoolean.vote_id == id).all()
        return statistic
    

def get_user_many_boolean(db: Session, id: int):
    vote = db.query(Vote).filter(Vote.vote_id == id)
    if vote.first() == None:
        raise HTTPException(status_code = 404, detail = f"Vote with id {id} is not found")
    else:
        options = db.query(Option).filter(Option.vote_id == id).all()
        option_ids = [option.option_id for option in options]
        list_user = []
        for option_id in option_ids:
            statistic = db.query(User, ResultManyBoolean.answer).join(ResultManyBoolean, ResultManyBoolean.user_id == User.user_id)\
                        .filter(ResultManyBoolean.option_id == option_id).all()
            list_user.append([option_id, statistic])
        return list_user
    