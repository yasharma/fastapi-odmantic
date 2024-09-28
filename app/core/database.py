from odmantic import AIOEngine
from motor.motor_asyncio import AsyncIOMotorClient

from core.config import config


def get_engine() -> AIOEngine:
    client = AsyncIOMotorClient(config.dbUrl)
    engine = AIOEngine(client=client, database="todo")
    return engine