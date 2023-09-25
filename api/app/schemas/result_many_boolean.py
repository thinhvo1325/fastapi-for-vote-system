from pydantic import BaseModel


class CreateResultManyBoolean(BaseModel):
    user_id: int
    option_id: int
    answer: str

class UpdateResultManyBoolean(BaseModel):
    answer: str