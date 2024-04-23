from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from redis.asyncio import Redis
from aiogram.fsm.storage.redis import RedisStorage, DefaultKeyBuilder


from bot.config import config

redis = Redis(host=config.redis.host, port=config.redis.port)
storage = RedisStorage(
    redis=redis,
    key_builder=DefaultKeyBuilder(with_bot_id=True)
)
bot = Bot(
    token=config.telegram.token,
    default=DefaultBotProperties(
        parse_mode=ParseMode.MARKDOWN_V2
    )
)
dp = Dispatcher(storage=storage)
