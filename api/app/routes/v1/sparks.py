from typing import Annotated

from app.core.db import SessionDep
from app.models.sparks import Spark, SparkCreate, SparkPublic
from fastapi import APIRouter, Query
from sqlmodel import select

router = APIRouter(prefix="/sparks")


@router.get("/")
def get_sparks(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[SparkPublic]:
    return session.exec(select(Spark).offset(offset).limit(limit)).all()


@router.post("/", response_model=SparkPublic)
def create_spark(model: SparkCreate, session: SessionDep):
    session.add(model)
    session.commit()
    session.refresh(model)
    return model
