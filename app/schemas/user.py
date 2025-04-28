from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.db.models import User
from app.core.security import hash_password

class UserCreate(BaseModel):
	email : str 
	password : str 

class UserResponse(BaseModel):
	id : int 
	email : str

	class Config: 
		from_attributes = True 

def CreateUserToUser(user : UserCreate):
	u = User()
	u.email = user.email
	u.hashed_password = hash_password(user.password)
	return u