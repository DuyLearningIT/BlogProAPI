from fastapi import APIRouter
from .auth import router as auth_router
from .posts import router as posts_router

router = APIRouter()

router.include_router(auth_router, prefix='/auth', tags=['auth'])
router.include_router(posts_router, prefix='/posts', tags=['posts'])
