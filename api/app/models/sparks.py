from sqlmodel import Field, SQLModel


class BaseSpark(SQLModel):
    name: str
    defence: int = Field(min_length=0, max_length=5)


class Spark(BaseSpark, table=True):
    id: int | None = Field(default=None, primary_key=True)


class SparkPublic(BaseSpark):
    id: int


class SparkCreate(BaseSpark):
    pass
