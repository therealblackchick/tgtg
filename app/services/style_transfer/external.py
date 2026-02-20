from app.services.style_transfer.base import StyledImage


class ExternalStyleTransferProvider:
    """
    Plug your AI API integration here.
    Expected behavior:
      1) send input bytes to external API
      2) receive stylized bytes
      3) return StyledImage
    """

    def __init__(
        self,
        api_url: str | None,
        api_key: str | None,
        timeout_seconds: float = 60.0,
    ) -> None:
        self._api_url = api_url
        self._api_key = api_key
        self._timeout_seconds = timeout_seconds

    async def stylize(self, image_bytes: bytes, filename: str) -> StyledImage:
        raise NotImplementedError(
            "External provider is not implemented yet. "
            "Add your AI API call in app/services/style_transfer/external.py"
        )
