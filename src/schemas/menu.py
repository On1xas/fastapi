from pydantic import BaseModel
from typing import Set, Tuple

class MenuSchema(BaseModel):
    id: int
    server_name: str
    spl_id: str
    spl_name: str
    last_version: int
    content_id_array: list

    class Config:
        from_attributes = True


class MIServersSchema(BaseModel):
    id: int
    server_name: str
    create_time: str

    class Config:
        from_attributes = True


class ContentSchema(BaseModel):
    id: int
    content_name: str
    content_id: str
    path: str
    create_time: str

    class Config:
        from_attributes = True

class ParsingSPL(BaseModel):
    playlist_name: str
    playlist_id: str
    last_spl_version: int
    content_list: Set[Tuple]