from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    bot_token: str = Field(alias="BOT_TOKEN")
    style_provider: str = Field(default="mock", alias="STYLE_PROVIDER")
    max_parallel_jobs: int = Field(default=100, alias="MAX_PARALLEL_JOBS", ge=1)
    ai_api_url: str | None = Field(default=None, alias="AI_API_URL")
    ai_api_key: str | None = Field(default=None, alias="AI_API_KEY")
    ai_timeout_seconds: float = Field(default=60.0, alias="AI_TIMEOUT_SECONDS")


def get_settings() -> Settings:
    return Settings()
