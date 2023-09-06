from src.utils.pasing_repository import ParsingSQLAlchemyRepository
from src.db.db import engines
from sqlalchemy.ext.asyncio import AsyncEngine

class ParsingMenuRepository(ParsingSQLAlchemyRepository):
    def __init__(self, server):
        self.engine: AsyncEngine = engines[server]
