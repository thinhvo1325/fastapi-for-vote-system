from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from ..database.MySQL import Base

class ResultManyBoolean(Base):
    __tablename__ = "result_many_boolean"

    user_id = Column(Integer, primary_key=True)
    option_id = Column(Integer, primary_key=True)
    answer = Column(String)
