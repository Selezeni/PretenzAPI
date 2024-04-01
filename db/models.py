from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker


Base = declarative_base()
engine = create_async_engine('sqlite+aiosqlite:///db/avesta.db', echo=True)
new_session = async_sessionmaker(engine, expire_on_commit=False)


class PdAct(Base):
    __tablename__ = 'pdact'

    vcode =  Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    nomer = Column(String(255), nullable=False, unique=True)
    matcode = Column(Integer, nullable=False)
    kolvo = Column(Integer, nullable=False)



async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all) 

