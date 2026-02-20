import asyncio

from app.services.style_transfer.base import StyleTransferProvider, StyledImage


class StyleTransferService:
    """
    Controls concurrent image stylization jobs in one bot process.
    """

    def __init__(
        self,
        provider: StyleTransferProvider,
        max_parallel_jobs: int,
    ) -> None:
        self._provider = provider
        self._limiter = asyncio.Semaphore(max_parallel_jobs)

    async def stylize(self, image_bytes: bytes, filename: str) -> StyledImage:
        async with self._limiter:
            return await self._provider.stylize(image_bytes=image_bytes, filename=filename)
