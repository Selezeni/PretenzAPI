import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

from app.models.models import Pretenz
from DB.schema import Avesta



app = FastAPI()
engine = create_engine('sqlite:///DB/avesta.db', echo=True)


@app.get("/")
async def root():
    with Session(bind=engine) as session:
        pretenz = session.query(Avesta).all()

    return pretenz


@app.post("/")
async def root(pretenz: Pretenz):

    # new_pretenz = Avesta(nomer = pretenz["nomer"], 
    #                         matcode = pretenz["matcode"],
    #                         kolvo = pretenz["kolvo"])
    
    print(pretenz.json())
    return {"message": f"Претензия успешно добавлена {pretenz.nomer}"}




if __name__ == '__main__':
    
    uvicorn.run(app, host='127.0.0.1', port=8000)