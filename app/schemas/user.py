from pydantic import BaseModel,Field, EmailStr
class UserCreate(BaseModel):
        name : str = Field(...,min_length=1,max_length=100)
        email :  EmailStr
        password: str = Field(..., min_length=6, max_length=100)

class UserResponse(BaseModel):
        id : int
        name  : str
        email : str

class UserUpdate(BaseModel):
        name: str | None = Field(None, min_length=1, max_length=100)
        email: EmailStr | None = None
        password: str | None = Field(None, min_length=6, max_length=100)        