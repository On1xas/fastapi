from abc import ABC, abstractmethod
from sqlalchemy import insert, select, delete
from sqlalchemy.ext.asyncio import AsyncEngine
from src.models.menu import Menu, Content

class MenuAbstractRepo(ABC):

    @abstractmethod
    async def set_menu():
        raise NotImplementedError
    @abstractmethod
    async def get_menu():
        raise NotImplementedError
    @abstractmethod
    async def delete_menu():
        raise NotImplementedError
    
    async def delete_all_menu():
        raise NotImplementedError




class MenuSQLAlchemyRepo(MenuAbstractRepo):
    model_menu: Menu = None
    engine: AsyncEngine = None

    async def set_menu(self, data):
        async with self.engine.connect() as session:
            stmt = insert(self.model_menu).values(**data).returning(self.model_menu.id)
            res = await session.execute(stmt)
            await session.commit()
            return res

    async def get_menu(self, server: str):
        async with self.engine.connect() as session:
            stmt = select(self.model_menu).where(self.model_menu.server_name == server)
            res = await session.execute(stmt)
            return res

    async def delete_menu(self, server:str, last_version: int):
        async with self.engine.connect() as session:
            stmt = delete(self.model_menu).where(self.model_menu.server_name == server).where(self.model_menu.last_version != last_version).returning(self.model_menu.id)
            res = await session.execute(stmt)
            await session.commit()
            return res

    async def delete_all_menu(self):
        async with self.engine.connect() as session:
            stmt = delete(self.model_menu)
            res = await session.execute(stmt)
            await session.commit()
            return res
            
class ContentAbstractRepo(ABC):

    @abstractmethod
    async def set_content():
        raise NotImplementedError


class ContentSQLAlchemyRepo(ContentAbstractRepo):
    model_content: Content = None
    engine: AsyncEngine = None

    async def set_content(self, data):
        async with self.engine.connect() as session:
            stmt = insert(self.model_content).values(**data)
            await session.execute(stmt)
            await session.commit()
