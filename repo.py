from sqlalchemy import select

from db.models import new_session, PdAct
from app.models.models import Pretenz, PretenzAdd


class PretenzRepo():

    @classmethod
    async def add_pretenz(cls, data: Pretenz) -> int:
        async with new_session() as session:
            pretenz_dict = data.model_dump()
            pretenz = PdAct(**pretenz_dict)
            session.add(pretenz)
            await session.flush()
            await session.commit()
        return pretenz.vcode
    
    
    @classmethod
    async def find_all(cls) -> list[Pretenz]:
        async with new_session() as session:
            query = select(PdAct)
            result = await session.execute(query)
            res_pretenz = result.scalars().all()
            #pretenz_schemas = [PretenzAdd.model_validate(pret) for pret in res_pretenz]
            return res_pretenz