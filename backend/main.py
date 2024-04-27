from fastapi import FastAPI

from backend.config import settings
from backend.config import init_db

app = FastAPI(title=settings.APP_NAME, description='API REST')

init_db()

if __name__ == '__main__':
    import uvicorn

    uvicorn.run('main:app')
