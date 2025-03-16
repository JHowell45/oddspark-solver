from sqlmodel import Field, SQLModel

from .core import DatetimeMixin


class AttackType(DatetimeMixin, table=True):
    name: str


class BaseSpark(SQLModel):
    name: str
    defence: int = Field(ge=0, le=5)
    offense: int = Field(ge=0, le=5)
    efficiency: int = Field(ge=0, le=5)
    capacity: int = Field(ge=0, le=5)


class Spark(DatetimeMixin, BaseSpark, table=True):
    pass


class SparkPublic(BaseSpark):
    id: int


class SparkCreate(BaseSpark):
    pass
