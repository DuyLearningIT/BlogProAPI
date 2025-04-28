from pydantic import BaseModel
from datetime import datatime
from .post import PostResponse

class UserCreate(BaseModel):
	email : str 
	password : str 

class UserResponse(BaseModel):
	id : int 
	email : str
	posts : List[PostResponse] = []

	class Config: 
		orm_mode = True 