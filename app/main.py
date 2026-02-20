import asyncio

from aiogram import Bot, Dispatcher

from app.bot.routers import setup_routers
from app.config import Settings, get_settings
from app.logging_config import setup_logging
from app.services.style_transfer.external import ExternalStyleTransferProvider
from app.services.style_transfer.mock import MockStyleTransferProvider
from app.services.style_transfer.service import StyleTransferService


def build_style_service(settings: Settings) -> StyleTransferService:
    provider_name = settings.style_provider.strip().lower()
    if provider_name == "external":
        provider = ExternalStyleTransferProvider(
            api_url=settings.ai_api_url,
            api_key=settings.ai_api_key,
            timeout_seconds=settings.ai_timeout_seconds,
        )
    elif provider_name == "mock":
        provider = MockStyleTransferProvider()
    else:
        raise ValueError(
            f"Unknown STYLE_PROVIDER='{settings.style_provider}'. "
            "Supported values: mock, external."
        )

    return StyleTransferService(
        provider=provider,
        max_parallel_jobs=settings.max_parallel_jobs,
    )


async def run_bot() -> None:
    setup_logging()
    settings = get_settings()
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()
    setup_routers(dp)

    style_service = build_style_service(settings)
    await dp.start_polling(
        bot,
        style_service=style_service,
        allowed_updates=dp.resolve_used_update_types(),
    )


if __name__ == "__main__":
    asyncio.run(run_bot())
