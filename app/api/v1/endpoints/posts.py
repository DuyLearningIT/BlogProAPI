from fastapi import APIRouter

router = APIRouter()

@router.get('/default')
async def default():
	return {
		'mess' : 'This is default getway of post router!'
	}