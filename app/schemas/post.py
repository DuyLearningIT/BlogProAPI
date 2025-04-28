from pydantic import BaseModel
from .user import UserResponse
from datetime import datetime 

class PostCreate(BaseModel):
	title : str 
	content : str
	owner_id : int 

class PostUpdate(BaseModel):
	title : str | None = None
	content : str | None = None
	owner_id : int | None = None

class PostResponse(BaseModel):
	id : int 
	title: str
	content : str
	owner_id : int
	owner : UserResponse
	created_at : datetime
	updated_at : datetime

	class Config: 
		from_attributes = True