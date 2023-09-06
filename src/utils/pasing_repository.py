from abc import ABC, abstractmethod
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncEngine

import logging

logger = logging.getLogger(__name__)


class ParsingAbstractRepository(ABC):

    @abstractmethod
    async def get_playlist_info():
        raise NotImplementedError

    @abstractmethod
    async def get_last_version_playlist():
        raise NotImplementedError

    @abstractmethod
    async def get_content_id_list():
        raise NotImplementedError

    @abstractmethod
    async def get_content_name():
        raise NotImplementedError

    @abstractmethod
    async def get_file_id():
        raise NotImplementedError
  

class ParsingSQLAlchemyRepository(ParsingAbstractRepository):
    engine: AsyncEngine = None

    async def get_playlist_info(self):
        query = 'SELECT playlist_id, playlist_name FROM mi_cms_info_playlist'
        async with self.engine.connect() as session:
            result = await session.execute(text(query))
            return result.fetchall()

    async def get_last_version_playlist(self, playlist_id):
            query = '''SELECT version_id FROM mi_cms_info_playlist_version WHERE is_active = 'Y' and playlist_id = :playlist_id
        '''
            async with self.engine.connect() as session:
                result = await session.execute(text(query),{"playlist_id": playlist_id})
                num = result.first()
                return int(num[0])

    async def get_content_id_list(self, playlist_id, last_version):
        async with self.engine.connect() as session:
            query = '''SELECT content_id  FROM mi_cms_map_playlist_content WHERE version_id = :last_version and playlist_id = :playlist_id
        '''
            result = await session.execute(text(query),{"playlist_id": playlist_id, "last_version": last_version})
            return result.fetchall()

    async def get_content_name(self, content_id):
        async with self.engine.connect() as session:
            query = '''SELECT content_name  FROM mi_cms_info_content WHERE content_id = :content_id
        '''
            result = await session.execute(text(query),{"content_id": content_id})
            return result.first()[0]

    async def get_file_id(self, content_id):
        async with self.engine.connect() as session:
            query = '''SELECT content_name  FROM mi_cms_info_content WHERE content_id = :content_id
        '''
            result = await session.execute(text(query),{"content_id": content_id})
            return result.fetchall()