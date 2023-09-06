import asyncio
import logging
import os
import sys

from src.main import server
from src.config.config import configparser, ConfigDB,ConfigServerEngine

logger = logging.getLogger("Cinema Manager Site")

async def start_app():
    logging.basicConfig(
        format="[%(asctime)s] [%(name)s] [%(levelname)s] > %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        level=logging.DEBUG,
)

    logger.debug("-> Site is online")
    
    await server.serve()

if __name__ == "__main__":
    asyncio.run(start_app())
    print("Site is down")

    