import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr, Field

BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

class Settings(BaseSettings):
    bot_token: SecretStr
    postgres_user: str
    postgres_password: str
    postgres_host: str = "localhost"
    postgres_port: int = 5432
    postgres_db: str
    admin_ids: list[int] = Field(default_factory=list)

    model_config = SettingsConfigDict(env_file=ENV_PATH, env_file_encoding='utf-8')

config = Settings()