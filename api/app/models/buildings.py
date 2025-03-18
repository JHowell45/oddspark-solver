from sqlmodel import Field, SQLModel


class BaseBuilding(SQLModel):
    name: str = Field(unique=True)


class Building(BaseBuilding, table=True):
    id: int | None = Field(default=None, primary_key=True)


class BaseRecipe(SQLModel):
    pass
