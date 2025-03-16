from typing import Annotated

from app.core.db import SessionDep
from app.models.sparks import (
    AttackType,
    AttackTypeCreate,
    AttackTypePublic,
    Spark,
    SparkCreate,
    SparkPublic,
)
from fastapi import APIRouter, Query
from sqlmodel import select

router = APIRouter(prefix="/sparks")
attack_type_router = APIRouter(prefix="/attack-type")

router.include_router(attack_type_router)


@router.get("/", response_model=list[SparkPublic])
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


@attack_type_router.get("/", response_model=list[AttackTypePublic])
def get_attack_types(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[AttackTypePublic]:
    return session.exec(select(AttackType).offset(offset).limit(limit)).all()


@attack_type_router.post("/", response_model=AttackTypePublic)
def create_attack_type(model: AttackTypeCreate, session: SessionDep):
    session.add(model)
    session.commit()
    session.refresh(model)
    return model
