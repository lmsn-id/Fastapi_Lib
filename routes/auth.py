from fastapi import APIRouter


router = APIRouter()
router.include_router(prefix="/api/auth", tags=["Auth"])
