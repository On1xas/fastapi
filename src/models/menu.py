import logging 

from sqlalchemy import VARCHAR, Integer, ARRAY, BigInteger, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from src.db.db import Base
from src.schemas.menu import MenuSchema, MIServersSchema, ContentSchema

logger = logging.getLogger(__name__)


class Menu(Base):
    __tablename__ = "menu"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    server_name: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
    spl_id: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
    spl_name: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
    last_version: Mapped[int] = mapped_column(Integer, nullable=True)
    content_id_array: Mapped[list] = mapped_column(ARRAY(VARCHAR(150)), nullable=True)
    create_time: Mapped[str] = mapped_column(DateTime, autoincrement=True)

    def to_read_model(self) -> MenuSchema:
        return MenuSchema(
            id=self.id,
            server_name=self.server_name,
            spl_id=self.spl_id,
            spl_name=self.spl_name,
            last_version=self.last_version,
            content_id_array=self.content_id_array
        )


class MIServers(Base):
    __tablename__ = 'mi_servers'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    server_name: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
    create_time: Mapped[str] = mapped_column(DateTime, autoincrement=True)

    def to_read_model(self) -> MIServersSchema:
        return MIServersSchema(
            id=self.id,
            server_name=self.server_name,
            create_time=self.create_time
        )


class Content(Base):
    __tablename__ = "content"

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    content_id: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
    content_name: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
    path: Mapped[str] = mapped_column(VARCHAR(50), nullable=True)
    create_time: Mapped[str] = mapped_column(DateTime, autoincrement=True)

    def to_read_model(self) -> ContentSchema:
        return ContentSchema(
            id=self.id,
            content_id=self.content_id,
            content_name=self.content_name,
            path=self.path,
            create_time=self.create_time
        )