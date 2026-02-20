from app.services.style_transfer.base import StyledImage


class MockStyleTransferProvider:
    """
    Temporary provider used before real AI integration.
    Returns the original image so end-to-end pipeline can be tested.
    """

    async def stylize(self, image_bytes: bytes, filename: str) -> StyledImage:
        return StyledImage(
            image_bytes=image_bytes,
            filename=f"ussr_{filename}",
            caption="Демо-режим: пока без AI, возвращаю исходник через боевой pipeline.",
        )
