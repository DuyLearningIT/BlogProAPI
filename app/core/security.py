from typing import Annotated
import jwt 
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from passlib.context import CryptContext
from jwt.exceptions import InvalidTokenError 
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
# ACCESS_TOKEN_EXPIRE_MINUTES = 30

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

def verify_password(plain_password, hashed_password):
	return pwd_context.verify(plain_password, hashed_password)

def hash_password(password):
	return pwd_context.hash(password)

def create_access_token(data: dict):
	to_encode = data.copy()
	expire = datetime.now() + timedelta(minutes=30)
	time = str(datetime.now())
	to_encode.update({'exp' : expire, 'accessed_time' : time})
	return jwt.encode(to_encode, SECRET_KEY, algorithm = ALGORITHM)

def get_current_user(token: str = Depends(oauth2_scheme)):
	credentials_exception = HTTPException(
		status_code=status.HTTP_401_UNAUTHORIZED,
		detail='Could not validate credentials',
		headers={'WWW-Authenticate' : 'Bearer'}
	)
	try:
		payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
		user_id = payload.get('id')
		if user_id is None:
			raise credentials_exception
		role: str = payload.get('role')
		if role is None:
			raise credentials_exception
		return {'id' : user_id, 'role' : role}
	except InvalidTokenError:
		raise credentials_exception

def admin_required(current_user: dict = Depends(get_current_user)):
	if current_user.get('role') != 'admin':
		raise HTTPException(
			status_code = status.HTTP_403_FORBIDDEN,
			detail = 'Admin access required'
		)
	return current_user