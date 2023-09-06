from src.utils.pasing_repository import ParsingAbstractRepository
from src.schemas.menu import ParsingSPL

class ParsingService:
    def __init__(
        self,
        parsing_menu_repo: ParsingAbstractRepository,
        server: str
        ):
        self.parsing_menu_repo: ParsingAbstractRepository = parsing_menu_repo
        
    async def get_menu(self):
        result = []
        for playlist_id, playlist_name in await self.parsing_menu_repo.get_playlist_info():
            spl=[]
            spl.append({
                "playlist_name": playlist_name,
                "playlist_id": playlist_id,
            })
            last_spl_version = await self.parsing_menu_repo.get_last_version_playlist(playlist_id)
            spl[0].update({"last_spl_version": last_spl_version})
            content_list = [(content_id[0], await self.parsing_menu_repo.get_content_name(content_id=content_id[0])) for content_id in await self.parsing_menu_repo.get_content_id_list(playlist_id=spl[0]['playlist_id'], last_version=spl[0]['last_spl_version'])]
            spl[0].update({"content_list": set(content_list)})
            result.append(ParsingSPL(**spl[0]))

        return result

    async def get_all_menu_miserver(self):
        pass

    async def update_spl_info(self):
        data = await self.get_menu()
        return data
    async def set_spl_info(self):
        pass
    async def clear_spl_info(self):
        pass