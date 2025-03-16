from sqlmodel import Field, SQLModel

from .core import DatetimeMixin


class BaseAttackType(SQLModel):
    name: str


class AttackType(DatetimeMixin, BaseAttackType, table=True):
    id: int | None = Field(default=None, primary_key=True)


class AttackTypePublic(DatetimeMixin, BaseAttackType):
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


class SparkPublic(DatetimeMixin, BaseSpark):
    id: int


class SparkCreate(BaseSpark):
    pass


class SparkPatch(BaseSpark):
    name: str | None = None
    defence: int | None = Field(ge=0, le=5, default=None)
    offense: int | None = Field(ge=0, le=5, default=None)
    efficiency: int | None = Field(ge=0, le=5, default=None)
    capacity: int | None = Field(ge=0, le=5, default=None)
