import asyncio
import logging

from bot.loader import bot, dp
from bot.handlers import user_handlers

logger = logging.getLogger(__name__)


async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format="%(filename)s:%(lineno)d #%(levelname)-8s "
               "[%(asctime)s] - %(name)s - %(message)s",
    )
    dp.include_routers(
        *user_handlers
    )
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
