import os
from pathlib import Path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr

# Жестко находим корень проекта и путь к .env
BASE_DIR = Path(__file__).resolve().parent.parent
ENV_PATH = BASE_DIR / ".env"

# Если Pydantic не найдет файл по этому пути, Python выкинет ошибку еще до запуска бота
if not ENV_PATH.exists():
    raise FileNotFoundError(f"Критическая ошибка: Файл .env не найден по пути {ENV_PATH}")

class Settings(BaseSettings):
    bot_token: SecretStr
    postgres_user: str
    postgres_password: str
    postgres_host: str = "localhost"
    postgres_port: int = 5449  # Твой порт Docker наружу
    postgres_db: str
    admin_ids: list[int]

    @property
    def database_url_asyncpg(self) -> str:
        # Для внутренней работы бота внутри сети Docker или локально:
        # Если бот запущен на Маке, он ломится на localhost:5449.
        return f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"

    model_config = SettingsConfigDict(
        env_file=str(ENV_PATH),
        env_file_encoding='utf-8',
        extra='ignore'
    )

config = Settings()