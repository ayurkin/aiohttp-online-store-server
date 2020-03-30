import asyncio
from aiohttp import web
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from umongo import MotorAsyncIOInstance


instance = MotorAsyncIOInstance()


async def init_mongo(mongodb_uri: str) -> AsyncIOMotorDatabase:
    loop = asyncio.get_event_loop()
    conn = AsyncIOMotorClient(mongodb_uri, io_loop=loop)
    return conn.get_database()


async def setup_mongo(app: web.Application) -> None:
    config = app['config']
    app['db'] = await init_mongo(config.MONGODB_URI)
    instance.init(app['db'])

    async def close_mongo(app: web.Application) -> None:
        app['db'].client.close()

    app.on_cleanup.append(close_mongo)
