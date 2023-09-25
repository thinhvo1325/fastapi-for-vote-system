from pydantic import BaseModel
from datetime import datetime
from ..models.vote import Status, Type
class CreateVote(BaseModel):
    name: str
    type: Type
    start_time: datetime
    end_time: datetime
    context: str
    status: Status
    user_id: int

class UpdateStatusVote(BaseModel):
    status: str
    
class UpdaeContextVote(BaseModel):
    context: str