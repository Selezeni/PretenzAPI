import uvicorn
from typing import Annotated
from fastapi import FastAPI, Depends
from app.models.models import Pretenz
from db.models import PdAct, create_tables, new_session
from contextlib import asynccontextmanager
from routers import router as pretenz_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    yield
    print("Перезагрузка приложения")


app = FastAPI(title="AvestaPretenzAPI", lifespan=lifespan)
app.include_router(pretenz_router)



if __name__ == '__main__':    
    uvicorn.run(app, host='127.0.0.1', port=8000)