from pydantic import BaseModel


class Pretenz(BaseModel):
    nomer: str
    matcode: int
    kolvo: int


class PretenzAdd(Pretenz):
    vcode: int