from sqlmodel import Field, Relationship, SQLModel


class BaseBuilding(SQLModel):
    name: str = Field(unique=True)


class Building(BaseBuilding, table=True):
    id: int | None = Field(default=None, primary_key=True)

    recipes: list["Recipe"] = Relationship(back_populates="building")


class BaseRecipe(SQLModel):
    building_id: int = Field(foreign_key="building.id", nullable=True)


class Recipe(BaseRecipe, table=True):
    id: int | None = Field(default=None, primary_key=True)

    building: Building = Relationship(back_populates="recipes")
