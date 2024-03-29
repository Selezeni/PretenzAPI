from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class Avesta(Base):
    __tablename__ = 'pdact'
    vcode = Column(Integer, nullable=False, unique=True, primary_key=True, autoincrement=True)
    nomer = Column(String(255), nullable=False, unique=True)
    matcode = Column(Integer, nullable=False)
    kolvo = Column(Integer, nullable=False)


    def __repr__(self):
        return f"Pretenz({self.nomer}, {self.matcode}, {self.kolvo})"



engine = create_engine('sqlite:///DB/avesta.db', echo=True)
Base.metadata.create_all(engine)
