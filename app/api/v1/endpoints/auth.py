from fastapi import APIRouter, HTTPException
from ....crud import get_user_crud, create_user_crud, login_crud, get_users
from app.db.database import db_depend
from app.schemas.user import UserResponse, UserCreate
from app.core.security import create_access_token

router = APIRouter()

@router.get('/default')
async def default():
	return {
		'mess' : 'This is default getway of auth router!'
	}

@router.get('/get-user')
async def read_user(db: db_depend, user_id : int):
	user = get_user_crud(db, user_id)
	if user:
		return {
			'mess' : 'Found user successfully !',
			'data' : {
				'id' : user.id,
				'email': user.email
			},
			'status_code' : 200
		}
	raise HTTPException(status_code= 404, detail = 'User not found !')


@router.post('/create-user')
async def create(db: db_depend, request: UserCreate):
	user = create_user_crud(db, request)
	if user == None:
		raise HTTPException(status_code= 400, detail='User has already exsisted, please try another one !')
	return {
		'mess' : "Created user successfullt !",
		'status_code' : 201,
		'data' : {
			'email' : user
		}
	}

@router.post('/login')
async def login(db : db_depend, request: UserCreate):
	check = login_crud(db, request)
	if check:
		return{
			'mess' : 'Login successfully !', 
			'access_token' : create_access_token({'id' : check.id, 'email' : check.email, 'role': check.role})
		}
	raise HTTPException(status_code=400, detail='Email or password was wrong ! Please try again !')


@router.get('/get-all-users')
async def getallusers(db : db_depend):
	try:
		result = get_users(db)
		return {
			'mess' : 'Get all users sucessfully !',
			'status_code' : 200,
			'data' : result
		}
	except Exception as ex:
		return {
			'mess' : f'Something was wrong : {ex}',
			'status_code' : 500
		}