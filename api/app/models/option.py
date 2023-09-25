from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from ..database.MySQL import Base

class Option(Base):
    __tablename__ = "option"

    option_id = Column(Integer, primary_key=True)
    vote_id = Column(Integer)
    content = Column(String)
