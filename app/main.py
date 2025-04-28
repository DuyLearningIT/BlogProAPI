from fastapi import FastAPI
from app.api.v1.endpoints import router as api_router
import uvicorn 

app = FastAPI()

# Include some router
app.include_router(api_router, prefix='/api/v1')

@app.get('/')
async def default():
	return {
		'mess' : 'API is running !',
		'status_code' : 200
	}

if __name__ == '__main__':
	uvicorn.run(app, host='localhost', port = 8080)