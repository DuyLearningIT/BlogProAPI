from app.db.models import Post
from app.schemas import PostCreate, PostResponse, PostDTOToPost, PostToPostDTO, PostUpdate
from sqlalchemy.orm import Session
from datetime import datetime

def get_all_posts_crud(db: Session):
	posts = db.query(Post).all()
	return posts

def get_post_id_crud(db: Session, post_id : int):
	post = db.query(Post).filter(Post.id == post_id).first()
	if post:
		return True, post
	return False, None

def create_post_crud(db: Session, request : PostCreate):
	db_post = PostDTOToPost(request)
	db.add(db_post)
	db.commit()
	db.refresh(db_post)
	return True, request

def update_post_crud(db: Session, request: PostUpdate):
	check = db.query(Post).filter(Post.id == request.id).first()
	if check == None:
		return False, None
	todict = request.__dict__
	for key, value in todict.items():
		if value is not None:
			setattr(check, key, value)
	check.updated_at = datetime.now()
	db.commit()
	db.refresh(check)
	return True, check

def delete_post_crud(db: Session, post_id : int):
	check = db.query(Post).filter(Post.id == post_id).first()
	if not check:
		return False
	db.delete(check)
	db.commit()
	return True
