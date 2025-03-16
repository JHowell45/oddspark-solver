from datetime import datetime, timezone

from sqlmodel import Field, SQLModel


class DatetimeMixin(SQLModel):
    id: int | None = Field(default=True, primary_key=True)
    created_at: datetime = Field(default=datetime.now(timezone.utc), nullable=False)
    updated_at: datetime = Field(default=datetime.now(timezone.utc), nullable=False)
