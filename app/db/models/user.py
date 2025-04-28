from sqlalchemy import Column, Integer, String, Boolean, DateTime
from datetime import datetime
from ..base import Base
from sqlalchemy.orm import relationship

class User(Base):
	__tablename__ = "user"

	id = Column(Integer, primary_key = True, index = True)
	email = Column(String(50), unique= True, nullable = False)
	hashed_password = Column(String(255), nullable = False)
	role = Column(String(10), default = 'user')
	is_active = Column(Boolean, default= True)
	created_at = Column(DateTime, default = datetime.utcnow)
	updated_at = Column(DateTime)
	
	posts = relationship('Post', back_populates='owner')