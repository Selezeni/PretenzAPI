import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
#from db.models import create_tables
#from contextlib import asynccontextmanager
from routers import router as pretenz_router


# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await create_tables()
#     yield
#     print("Перезагрузка приложения")


app = FastAPI(title="AvestaPretenzAPI")
app.include_router(pretenz_router)

@app.get("/")
async def page_index():
    return FileResponse("app/templates/index.html")

if __name__ == '__main__':    
    uvicorn.run(app, host='127.0.0.1', port=8000)