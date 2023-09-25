from pydantic import BaseModel

class User(BaseModel):
    user_id: int
    name: str
    email: str
    phone: str

class CreateUser(BaseModel):
    name: str
    email: str
    phone: str