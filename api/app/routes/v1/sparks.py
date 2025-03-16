from typing import Annotated

from app.core.db import SessionDep
from app.core.exceptions import not_found_exception
from app.models.sparks import (
    AttackType,
    AttackTypeCreate,
    AttackTypePublic,
    Spark,
    SparkCreate,
    SparkPatch,
    SparkPublic,
)
from fastapi import APIRouter, Path, Query
from sqlmodel import select

router = APIRouter(prefix="/sparks")
attack_type_router = APIRouter(prefix="/attack-type")


@router.get("/", response_model=list[SparkPublic])
def get_sparks(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[SparkPublic]:
    return session.exec(select(Spark).offset(offset).limit(limit)).all()


@router.post("/", response_model=SparkPublic)
def create_spark(model: SparkCreate, session: SessionDep) -> SparkPublic:
    db_model = AttackType.model_validate(model)
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return db_model


@router.patch("/{spark_id}", response_model=SparkPublic)
def update_spark(
    spark_id: Annotated[int, Path(gt=0)], model: SparkPatch, session: SessionDep
) -> SparkPublic:
    if db_model := session.get(Spark, spark_id):
        model_data = model.model_dump(exclude_unset=True)
        db_model.sqlmodel_update(model_data)
        session.add(db_model)
        session.commit()
        session.refresh(db_model)
        return db_model
    return not_found_exception


@router.delete("/{spark_id}")
def delete_spark(spark_id: Annotated[int, Path(gt=0)], session: SessionDep):
    if db_model := session.get(Spark, spark_id):
        session.delete(db_model)
        session.commit()
        return {"ok": True}
    return not_found_exception


@attack_type_router.get("/", response_model=list[AttackTypePublic])
def get_attack_types(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[AttackTypePublic]:
    return session.exec(select(AttackType).offset(offset).limit(limit)).all()


@attack_type_router.post("/", response_model=AttackTypePublic)
def create_attack_type(model: AttackTypeCreate, session: SessionDep):
    db_model = AttackType.model_validate(model)
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return db_model


router.include_router(attack_type_router)
