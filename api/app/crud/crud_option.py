from typing import List
from sqlalchemy.orm import Session
from ..models.option import Option
from ..schemas.option import CreateOption

def get_option_by_vote_id(db: Session, vote_id: int):
    return db.query(Option).filter(Option.vote_id == vote_id).all()

def create_option(db: Session, request: CreateOption):
    new_option = Option(
        vote_id = request.vote_id,
        content = request.content,
    )
    db.add(new_option)
    db.commit()
    db.refresh(new_option)
    return new_option