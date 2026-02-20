from aiogram import Dispatcher

from app.bot.handlers.common import router as common_router
from app.bot.handlers.photos import router as photos_router


def setup_routers(dp: Dispatcher) -> None:
    dp.include_router(common_router)
    dp.include_router(photos_router)
