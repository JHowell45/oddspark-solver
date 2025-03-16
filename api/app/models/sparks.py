from sqlmodel import Field, SQLModel

from .base import BaseModel


class AttackType(BaseModel, table=True):
    name: str


class BaseSpark(SQLModel):
    name: str
    defence: int = Field(ge=0, le=5)
    offense: int = Field(ge=0, le=5)
    efficiency: int = Field(ge=0, le=5)
    capacity: int = Field(ge=0, le=5)


class Spark(BaseModel, BaseSpark, table=True):
    pass


class SparkPublic(BaseSpark):
    id: int


class SparkCreate(BaseSpark):
    pass
