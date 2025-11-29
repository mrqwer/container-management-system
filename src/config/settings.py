import os
from pathlib import Path
from dotenv import load_dotenv


ROOT_PATH = Path(__file__).resolve().parents[2]
load_dotenv(ROOT_PATH)


class Settings:
    POSTGRES_USER: str = os.environ.get("POSTGRES_USER", "user")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD", "password")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST", "postgres")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT", "5432")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB", "warehouse")
    DB_ECHO_LOG: bool = False

    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )


settings = Settings()

