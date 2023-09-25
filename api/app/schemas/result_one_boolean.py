from pydantic import BaseModel


class CreateResultOneBoolean(BaseModel):
    user_id: int
    vote_id: int
    answer: str

class UpdateResultOneBoolean(BaseModel):
    answer: str