from src.models.menu import Menu, Content
from src.utils.menu_repository import MenuSQLAlchemyRepo, ContentSQLAlchemyRepo
from src.db.db import engines
from sqlalchemy.ext.asyncio import AsyncEngine

class MenuRepository(MenuSQLAlchemyRepo):
    def __init__(self):
        self.model_menu = Menu
        self.engine: AsyncEngine = engines["fastapi"]


class ContentReposytory(ContentSQLAlchemyRepo):
    def __init__(self):
        self.model_content = Content
        self.engine: AsyncEngine = engines["fastapi"]

