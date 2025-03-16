from fastapi import APIRouter

router = APIRouter(prefix="/sparks")


@router.get("/")
def get_sparks() -> list:
    return []
