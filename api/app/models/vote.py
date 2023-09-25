import enum
from sqlalchemy import  Column, Enum
from sqlalchemy.sql.sqltypes import Integer, String, DateTime
from sqlalchemy.sql import func
from ..database.MySQL import Base

class Type(enum.Enum):
    one_select = "one_select"
    many_select = "many_select"
    one_bolean = "one_bolean"
    many_bolean = "many_bolean"

class Status(enum.Enum):
    upcoming = "upcoming"
    ongoing = "ongoing"
    completed = "completed"
    
class Vote(Base):
    __tablename__ = "vote"

    vote_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    type = Column(Enum(Type), default=Type.one_select)
    start_time = Column(DateTime(timezone=True))
    end_time = Column(DateTime(timezone=True))
    context = Column(String)
    status = Column(Enum(Status), default=Status.upcoming)
    time_created = Column(DateTime(timezone=True), default=func.now())
    user_id = Column(Integer)