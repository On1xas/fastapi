from dataclasses import dataclass
import environs


@dataclass
class ConfigDB:
    driver: str
    host: str
    port: str
    user: str
    password: str
    database: str

@dataclass
class ConfigServerEngine:
    driver_engine: str
    host_arena: str
    port_arena: str
    host_dana_81: str
    port_dana_81: str
    host_dana_80: str
    port_dana_80: str
    host_plz_131: str
    port_plz_131: str
    host_plz_132: str
    port_plz_132: str
    host_triniti: str
    port_triniti: str
    user_engine: str
    password_engine: str
    database_engine: str
    user_engine: str
    password_engine: str

@dataclass
class ConfigRedis:
    redis_host: str
    redis_port: str
    redis_db: str

def configparser(path):
    parser = environs.Env()
    parser.read_env(path)
    return (ConfigDB(
        driver=parser('driver'),
        host=parser('host'),
        port=parser('port'),
        user=parser('user'),
        password=parser('password'),
        database=parser('database')
    ),
        ConfigServerEngine(
            driver_engine=parser('driver_engine'),
            host_arena=parser('host_arena'),
            port_arena=parser('port_arena'),
            host_dana_81=parser('host_dana_81'),
            port_dana_81=parser('port_dana_81'),
            host_dana_80=parser('host_dana_80'),
            port_dana_80=parser('port_dana_80'),
            host_plz_131=parser('host_plz_131'),
            port_plz_131=parser('port_plz_131'),
            host_plz_132=parser('host_plz_132'),
            port_plz_132=parser('port_plz_132'),
            host_triniti=parser('host_triniti'),
            port_triniti=parser('port_triniti'),
            user_engine=parser('user_engine'),
            password_engine=parser('password_engine'),
            database_engine=parser('database_engine')
        ),
        ConfigRedis(
            redis_host=parser('redis_host'),
            redis_port=parser('redis_port'),
            redis_db=parser('redis_db')
        )
    )
