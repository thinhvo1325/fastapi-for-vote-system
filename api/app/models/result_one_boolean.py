from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from ..database.MySQL import Base

class ResultOneBoolean(Base):
    __tablename__ = "result_one_boolean"

    user_id = Column(Integer, primary_key=True)
    vote_id = Column(Integer, primary_key=True)
    answer = Column(String)
