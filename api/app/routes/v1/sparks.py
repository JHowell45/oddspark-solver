from app.core.db import get_session
from app.models.sparks import SparkPublic
from fastapi import APIRouter, Depends

router = APIRouter(prefix="/sparks")


@router.get("/")
def get_sparks() -> list:
    return []


@router.post("/", response_model=SparkPublic)
def create_spark(session: Depends[get_session]):
    pass
