import logging

from sqlmodel import SQLModel, create_engine

from config import settings
from backend.schemas.entities import *

connect_args = {"check_same_thread": False}
engine = create_engine(str(settings.database_uri), echo=True)

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)


def init_db():
    try:
        logger.info('Init db')
        SQLModel.metadata.create_all(engine)
    except Exception as ex:
        logger.info(f'Error while connect to db: {ex}')
