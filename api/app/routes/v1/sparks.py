from typing import Annotated

from app.core.db import SessionDep
from app.core.exceptions import not_found_exception
from app.models.sparks import (
    AttackType,
    AttackTypeCreate,
    AttackTypePublicWithSparks,
    Spark,
    SparkCreate,
    SparkPatch,
    SparkPublicWithAttackType,
)
from fastapi import APIRouter, Path, Query
from sqlmodel import select

router = APIRouter(prefix="/sparks")
attack_type_router = APIRouter(prefix="/attack-type")


@router.get("/", response_model=list[SparkPublicWithAttackType])
def get_sparks(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[SparkPublicWithAttackType]:
    return session.exec(select(Spark).offset(offset).limit(limit)).all()


@router.post("/", response_model=SparkPublicWithAttackType)
def create_spark(model: SparkCreate, session: SessionDep) -> SparkPublicWithAttackType:
    db_model = Spark.model_validate(model)
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return db_model


@router.patch("/{spark_id}", response_model=SparkPublicWithAttackType)
def update_spark(
    spark_id: Annotated[int, Path(gt=0)], model: SparkPatch, session: SessionDep
) -> SparkPublicWithAttackType:
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


@attack_type_router.get("/", response_model=list[AttackTypePublicWithSparks])
def get_attack_types(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[AttackTypePublicWithSparks]:
    return session.exec(select(AttackType).offset(offset).limit(limit)).all()


@attack_type_router.post("/", response_model=AttackTypePublicWithSparks)
def create_attack_type(
    model: AttackTypeCreate, session: SessionDep
) -> AttackTypePublicWithSparks:
    db_model = AttackType.model_validate(model)
    session.add(db_model)
    session.commit()
    session.refresh(db_model)
    return db_model


router.include_router(attack_type_router)
