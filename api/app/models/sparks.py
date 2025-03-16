from sqlmodel import Field, SQLModel

from .core import DatetimeMixin


class BaseAttackType(SQLModel):
    name: str


class AttackType(DatetimeMixin, BaseAttackType, table=True):
    id: int | None = Field(default=None, primary_key=True)


class AttackTypePublic(BaseAttackType):
    id: int


class AttackTypeCreate(BaseAttackType):
    pass


class BaseSpark(SQLModel):
    name: str
    defence: int = Field(ge=0, le=5)
    offense: int = Field(ge=0, le=5)
    efficiency: int = Field(ge=0, le=5)
    capacity: int = Field(ge=0, le=5)


class Spark(DatetimeMixin, BaseSpark, table=True):
    id: int | None = Field(default=None, primary_key=True)


class SparkPublic(BaseSpark):
    id: int


class SparkCreate(BaseSpark):
    pass
