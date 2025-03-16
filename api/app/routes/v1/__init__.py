from fastapi import APIRouter

from .sparks import router as sparks_router

router = APIRouter(prefix="/v1")
router.include_router(sparks_router)
