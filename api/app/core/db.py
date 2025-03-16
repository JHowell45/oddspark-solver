from typing import Generator

from app.core.config import get_settings
from sqlmodel import Session, create_engine

engine = create_engine(get_settings().DATABASE_URI, echo=False)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session
