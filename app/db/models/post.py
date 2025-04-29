from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from ..base import Base
from .user import User

class Post(Base):
	__tablename__ = 'post'

	id = Column(Integer, primary_key= True, index=True)
	title = Column(String(100), nullable = False )
	content = Column(String(255), nullable = False)
	owner_id = Column(Integer, ForeignKey('user.id'))
	owner = relationship('User', back_populates='posts', foreign_keys=[owner_id])
	created_at = Column(DateTime, default = datetime.utcnow)
	updated_at = Column(DateTime)