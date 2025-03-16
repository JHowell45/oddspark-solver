from typing import Annotated, Generator

from app.core.config import get_settings
from fastapi import Depends
from sqlmodel import Session, create_engine

engine = create_engine(str(get_settings().DATABASE_URI), echo=False)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
