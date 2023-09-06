from src.utils.menu_repository import MenuAbstractRepo, ContentAbstractRepo
from src.utils.redis_repository import RedisDB, RedisAbstrastRepository
from src.schemas.menu import ParsingSPL
from typing import List
import datetime

class MenuService:
    def __init__(
        self,
        menu_repo: MenuAbstractRepo,
        content_repo: ContentAbstractRepo,
        redis_repo: RedisAbstrastRepository,
        server: str
    ):
        self.menu_repo: MenuAbstractRepo = menu_repo
        self.content_repo: ContentAbstractRepo = content_repo
        self.redis_repo: RedisAbstrastRepository = redis_repo
        self.server: str = server

    async def update_menu(self, data: List[ParsingSPL]):
        for spl in data:
            # Обрабатываем контент плейлиста
            content_id: List = []
            for content in spl.content_list:
                content_id.append(content[0])
                ## Добавить проверку на повторы контента по ID
                ## Добавить функцию формирования path к изображения контента
                await self.content_repo.set_content({
                    "content_id": content[0],
                    "content_name": content[1],
                    "path": None,
                    "create_time": datetime.datetime.now()
                })
            # Записываем данные в таблицу
            ## Добавить проверку на наличие SPL такой версии в таблице
            await self.menu_repo.set_menu({
                "server_name": self.server,
                "spl_id": spl.playlist_id,
                "spl_name": spl.playlist_name,
                "last_version": spl.last_spl_version,
                "content_id_array": content_id,
                "create_time": datetime.datetime.now()
            })

    async def delete_all(self):
        await self.menu_repo.delete_all_menu()
    
