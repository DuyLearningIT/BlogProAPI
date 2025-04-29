from fastapi import APIRouter, HTTPException
from app.db.database import db_depend
from app.crud import get_all_posts_crud, get_post_id_crud, delete_post_crud, update_post_crud, create_post_crud
from app.schemas import PostCreate, PostUpdate

router = APIRouter()

@router.get('/default')
async def default():
	return {
		'mess' : 'This is default getway of post router!'
	}

@router.get('/get-all-posts')
async def get_all_posts(db: db_depend):
	try:
		result = get_all_posts_crud(db)
		return {
			'mess' : 'Get all posts sucessfully !',
			'data' : result,
			'status_code' : 200
		}
	except Exception as ex:
		return {
			'mess' : 'Something was wrong !',
			'status_code' : 500
		}
	
@router.get('/get-post')
async def get_post(db: db_depend, post_id: int):
	check, data = get_post_id_crud(db, post_id)
	if check:
		return {
			'mess' : 'Get post successfully !',
			'data' : data,
			'status_code' : 200
		}
	raise HTTPException(status_code=400, detail='Post not found !')

@router.post('/create')
async def create_post(db: db_depend, request : PostCreate):
	check, data = create_post_crud(db, request)
	if check:
		return {
			'mess': 'Created post succesfully !',
			'status_code' : 201,
			'data' : data
		}
	raise HTTPException(status_code= 400, detail='Something was wrong !')

@router.post('/update')
async def update_post(db: db_depend, request: PostUpdate):
	check, data = update_post_crud(db, request)
	if check:
		return {
			'mess' : 'Updated post successfully !',
			'data' : data,
			'status_code' : 200
		}
	# raise HTTPException(status_code=400, detail= 'Something was wrong !')

@router.delete('/delete')
async def delete_post(db : db_depend, post_id : int):
	result = delete_post_crud(db, post_id)
	if result: 
		return{
			'mess' : 'Deleted post successfully !',
			'status_code' : 204
		}
	raise HTTPException(status_code=400, detail='Something was wrong !')
