from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("start"))
async def start_handler(message: Message) -> None:
    await message.answer(
        "Привет! Пришли фотографию, и я верну её в стиле плакатов СССР.\n\n"
        "Сейчас включён каркасный режим: провайдер стиля можно подключить отдельно."
    )


@router.message(Command("help"))
async def help_handler(message: Message) -> None:
    await message.answer(
        "Как пользоваться:\n"
        "1) Отправь фото.\n"
        "2) Подожди обработку.\n"
        "3) Получи результат.\n\n"
        "Чтобы подключить реальный AI, замени внешнего провайдера в app/services/style_transfer/external.py."
    )
