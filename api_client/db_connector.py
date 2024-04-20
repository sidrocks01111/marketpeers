"""
connector for the mongodb databse
"""
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie

from api_client.config import constants
from controller.db.db_models import ListedStocksIndia, allStocksSymbols

client = AsyncIOMotorClient(constants.MONGODB_HOST)
db = client.marketPeerDB


async def init_mongodb():
    """
    initializing all the models in mongodb
    """
    await init_beanie(
        database=db, document_models=[
            ListedStocksIndia,
            allStocksSymbols
        ]
    )
