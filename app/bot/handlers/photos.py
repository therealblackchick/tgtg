import io
import logging
from pathlib import Path

from aiogram import Bot, Router
from aiogram.exceptions import TelegramBadRequest
from aiogram.types import BufferedInputFile, Message

from app.services.style_transfer.base import StyledImage
from app.services.style_transfer.service import StyleTransferService

router = Router()
logger = logging.getLogger(__name__)


@router.message(lambda message: bool(message.photo))
async def photo_handler(
    message: Message,
    bot: Bot,
    style_service: StyleTransferService,
) -> None:
    if not message.photo:
        await message.answer("Нужно отправить фото.")
        return

    status = await message.answer("Фото получено. Запускаю стилизацию...")

    photo = message.photo[-1]
    source_file = await bot.get_file(photo.file_id)
    if not source_file.file_path:
        await status.edit_text("Не удалось скачать файл из Telegram. Попробуйте другое фото.")
        return

    source_name = Path(source_file.file_path).name or f"{photo.file_id}.jpg"

    source_stream = io.BytesIO()
    await bot.download_file(source_file.file_path, destination=source_stream)

    try:
        result: StyledImage = await style_service.stylize(
            image_bytes=source_stream.getvalue(),
            filename=source_name,
        )
    except NotImplementedError:
        await status.edit_text(
            "Внешний AI провайдер ещё не подключён. "
            "Добавьте реализацию в app/services/style_transfer/external.py."
        )
        return
    except Exception:
        logger.exception("Failed to stylize image")
        await status.edit_text(
            "Не удалось обработать фото. Проверьте настройки провайдера и повторите попытку."
        )
        return

    await message.answer_photo(
        photo=BufferedInputFile(
            file=result.image_bytes,
            filename=result.filename,
        ),
        caption=result.caption,
    )
    try:
        await status.delete()
    except TelegramBadRequest:
        logger.debug("Status message was not deleted")


@router.message()
async def fallback_handler(message: Message) -> None:
    await message.answer("Отправь фото или используй /help.")
