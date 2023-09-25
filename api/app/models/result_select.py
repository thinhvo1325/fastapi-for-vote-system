from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer
from ..database.MySQL import Base

class ResultSelect(Base):
    __tablename__ = "result_select"

    user_id = Column(Integer, primary_key=True)
    option_id = Column(Integer, primary_key=True)
    
