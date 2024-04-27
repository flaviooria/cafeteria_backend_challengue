from fastapi import Depends
from sqlmodel import Session
from typing_extensions import Annotated, Generator

from backend.config import engine


def get_session_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDependency = Annotated[Session, Depends(get_session_db)]
