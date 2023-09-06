from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
from src.config.config import configparser
import redis

engine = create_async_engine(
    "postgresql+asyncpg://magicinfo:magicinfo@192.168.95.83:5432/magicinfo"
)
config_db, config_engine, config_redis = configparser(".env")

engines = {
    "parsing": create_async_engine("postgresql+asyncpg://magicinfo:magicinfo@192.168.95.83:5432/magicinfo"),
    "fastapi": create_async_engine(f"{config_db.driver}://{config_db.user}:{config_db.password}@{config_db.host}:{config_db.port}/{config_db.database}"),
    "arena": create_async_engine(f"{config_engine.driver_engine}://{config_engine.user_engine}:{config_engine.password_engine}@{config_engine.host_arena}:{config_engine.port_arena}/{config_engine.database_engine}"),
    "dana81": create_async_engine(f"{config_engine.driver_engine}://{config_engine.user_engine}:{config_engine.password_engine}@{config_engine.host_dana_81}:{config_engine.port_dana_81}/{config_engine.database_engine}"),
    "dana80": create_async_engine(f"{config_engine.driver_engine}://{config_engine.user_engine}:{config_engine.password_engine}@{config_engine.host_dana_80}:{config_engine.port_dana_80}/{config_engine.database_engine}"),
    "plz131": create_async_engine(f"{config_engine.driver_engine}://{config_engine.user_engine}:{config_engine.password_engine}@{config_engine.host_plz_131}:{config_engine.port_plz_131}/{config_engine.database_engine}"),
    "plz132": create_async_engine(f"{config_engine.driver_engine}://{config_engine.user_engine}:{config_engine.password_engine}@{config_engine.host_plz_132}:{config_engine.port_plz_132}/{config_engine.database_engine}"),
    "triniti": create_async_engine(f"{config_engine.driver_engine}://{config_engine.user_engine}:{config_engine.password_engine}@{config_engine.host_triniti}:{config_engine.port_triniti}/{config_engine.database_engine}")
}

redis_tools = redis.Redis(
    host=config_redis.redis_host,
    port=config_redis.redis_port,
    db=config_redis.redis_db,
    charset="utf-8",
    decode_responses=True
)


class Base(DeclarativeBase):
    pass
