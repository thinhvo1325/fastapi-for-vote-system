from pydantic import BaseModel


class CreateResultSelect(BaseModel):
    user_id: int
    option_id: int

class UpdateResultSelect(BaseModel):
    option_id: int