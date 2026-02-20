from dataclasses import dataclass
from typing import Protocol


@dataclass(slots=True)
class StyledImage:
    image_bytes: bytes
    filename: str
    caption: str = "Готово: версия в стиле СССР."


class StyleTransferProvider(Protocol):
    async def stylize(self, image_bytes: bytes, filename: str) -> StyledImage:
        """Transform input image bytes and return styled bytes."""
