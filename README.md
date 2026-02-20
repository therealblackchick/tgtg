# USSR Style Telegram Bot (Skeleton)

Современный каркас Telegram-бота на `aiogram 3`, рассчитанный на одновременную работу с большим количеством пользователей.

## Что уже сделано

- Асинхронный бот (`aiogram`) с обработчиками `/start`, `/help` и фото.
- Сервисный слой `StyleTransferService` с ограничением параллельности через `asyncio.Semaphore`.
- Провайдеры стилизации:
  - `MockStyleTransferProvider` — заглушка (пока возвращает исходное фото).
  - `ExternalStyleTransferProvider` — место для подключения вашего AI API.
- Конфигурация через переменные окружения (`.env`), без хардкода токена в git.

## Структура

```text
app/
  main.py
  config.py
  logging_config.py
  bot/
    routers.py
    handlers/
      common.py
      photos.py
  services/
    style_transfer/
      base.py
      service.py
      mock.py
      external.py
```

## Быстрый старт

1. Установить зависимости:

   ```bash
   pip install -e .
   ```

2. Создать `.env` на основе примера:

   ```bash
   cp .env.example .env
   ```

3. Вписать токен бота в `.env`:

   ```env
   BOT_TOKEN=ваш_токен
   STYLE_PROVIDER=mock
   MAX_PARALLEL_JOBS=100
   ```

4. Запустить бота:

   ```bash
   python -m app.main
   ```

## Куда добавлять AI API

Откройте файл:

`app/services/style_transfer/external.py`

И реализуйте метод:

`ExternalStyleTransferProvider.stylize(...)`

После этого переключите:

```env
STYLE_PROVIDER=external
AI_API_URL=...
AI_API_KEY=...
```
