from sqlalchemy import Column
from sqlalchemy.sql.sqltypes import Integer, String
from ..database.MySQL import Base

class User(Base):
    __tablename__ = "user"

    user_id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True)
    phone = Column(String, unique=True)