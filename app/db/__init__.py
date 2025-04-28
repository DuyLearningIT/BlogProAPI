from .models import User, Post
from .base import Base
from .session import engine

Base.metadata.create_all(bind=engine)
