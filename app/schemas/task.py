from pydantic import BaseModel,Field
from typing import Literal
class TaskCreate(BaseModel):
    title : str = Field(..., min_length=1, max_length=100)
    description : str | None = None
    user_id: int = Field(..., gt=0)

class TaskResponse(BaseModel):
    id : int
    title : str
    description : str | None = None
    status : str 
    user_id : int

class TaskUpdate(BaseModel):
    title: str | None = Field(None, min_length=1, max_length=100)
    description: str | None = None
    status: Literal["todo", "in_progress", "done"] | None = None
    
    