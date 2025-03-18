from app.models.core import DatetimeMixin
from sqlmodel import Field, SQLModel


class BaseItem(SQLModel):
    name: str = Field(unique=True)


class Item(DatetimeMixin, BaseItem, table=True):
    id: int | None = Field(default=None, primary_key=True)
