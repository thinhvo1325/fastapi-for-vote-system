from pydantic import BaseModel

class CreateOption(BaseModel):
    vote_id: int
    content: str