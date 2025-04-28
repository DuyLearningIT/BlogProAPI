from typing import Annotated
import jwt 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jwt.exceptions import InvalidTokenError 
from datetime import datetime

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def verify_password(plain_password, hashed_password):
	return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
	return pwd_context.hash(password)

def create_access_token(data: dict):
	to_encode = data.copy()
	expire = ACCESS_TOKEN_EXPIRE_MINUTES
	time = str(datetime.now())
	to_encode.update({'exp' : expire, 'accessed_time' : time})
	return jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)