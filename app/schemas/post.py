from pydantic import BaseModel
from .user import UserResponse
from datetime import datetime 
from app.db.models import Post

class PostCreate(BaseModel):
	title : str 
	content : str
	owner_id : int 

class PostUpdate(BaseModel):
	id : int
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

def PostToPostDTO(post : Post):
	p = PostCreate()
	p.title = post.title
	p.content = post.content
	p.owner_id = post.owner_id
	return p

def PostDTOToPost(post: PostCreate):
	p = Post(**post.dict())
	return p