from ..schemas import UserCreate, CreateUserToUser
from ..db.models import User 
from sqlalchemy.orm import Session 
from ..core import *
from app.db.database import db_depend
from app.core.security import verify_password

def create_user_crud(db: Session, user: UserCreate):
	check = db.query(User).filter(User.email == user.email).first()
	if check:
		return None
	db_user = CreateUserToUser(user)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)
	return db_user

def get_user_crud(db: Session, user_id : int):
	return db.query(User).filter(User.id == user_id).first()

def login_crud(db: Session, user: UserCreate):
	check = db.query(User).filter(User.email == user.email).first()
	if check:
		if verify_password(user.password, check.hashed_password):
			return check
		return None
	return None

def get_users(db: Session):
	list_users = db.query(User).all()
	return list_users