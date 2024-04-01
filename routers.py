from typing import Annotated
from fastapi import APIRouter, Depends
from app.models.models import Pretenz
from repo import PretenzRepo

router = APIRouter(
    prefix="/pretenz",
    tags=["Претензии"],
)

@router.post("")
async def add_new_pretenz(
    pretenz: Annotated[Pretenz, Depends()]
    ) -> list[dict]:
    vcode = await PretenzRepo.add_pretenz(pretenz)
    return {"sattus": "200 ok", "document": vcode}


@router.get("")
async def get_pretenz()-> list[Pretenz]:
    all_pretenz = await PretenzRepo.find_all()
    return all_pretenz