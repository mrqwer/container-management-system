from functools import lru_cache
from typing import Literal, Optional
from dotenv import load_dotenv
import os
from helper import current_dir
from pydantic import PostgresDsn


dotenv_path = os.path.join(current_dir, "src\config\.env")
load_dotenv(dotenv_path)


class Settings:
    ENVIRONMENT: Literal["dev", "pro"] = "dev"
    DB_ECHO: bool = True
    TITLE: str = os.environ.get("TITLE")
    DESCRIPTION: str = os.environ.get("DESCRIPTION")
    API_V1_STR: str = "/v1"
    VERSION: str = "1.0.0"
    DEBUG: bool = os.environ.get("DEBUG")
    SECRET_KEY: str = os.environ.get("SECRET_KEY")
    CORS_ALLOWED_ORIGINS: str = os.environ.get("CORS_ALLOWED_ORIGINS")
    OPENAPI_PREFIX: str = os.environ.get("OPENAPI_PREFIX")
    DOCS_URL: str = "/docs"
    REDOC_URL: str = "/redoc"
    OPENAPI_URL: str = "/api"

    DATETIME_TIMEZONE: str = "Asia/Almaty"
    DATETIME_FORMAT: str = "%Y-%m-%d %H:%M:%S"

    TOKEN_ALGORITHM: str = "HS256"
    TOKEN_EXPIRE_SECONDS: int = 60 * 60 * 24 * 1
    TOKEN_REFRESH_EXPIRE_SECONDS: int = 60 * 60 * 24 * 7
    TOKEN_URL_SWAGGER: str = f"{API_V1_STR}/auth/swagger_login"
    TOKEN_EXCLUDE: list[str] = [
        f"{API_V1_STR}/auth/login",
    ]
    USER_TYPE_EXCLUDE: list[str] = [
        # f'{API_V1_STR}/requisition/create',
        f"{API_V1_STR}/user/register"
    ]
    LOG_STDOUT_FILENAME: str = "ce_access.log"
    LOG_STDERR_FILENAME: str = "ce_error.log"

    LIMITER_REDIS_PREFIX: str = "ce_limiter"

    MIDDLEWARE_CORS: bool = True
    MIDDLEWARE_GZIP: bool = True
    MIDDLEWARE_ACCESS: bool = False

    POSTGRES_USER: str = os.environ.get("POSTGRES_USER")
    POSTGRES_PASSWORD: str = os.environ.get("POSTGRES_PASSWORD")
    POSTGRES_HOST: str = os.environ.get("POSTGRES_HOST")
    POSTGRES_PORT: str = os.environ.get("POSTGRES_PORT")
    POSTGRES_DB: str = os.environ.get("POSTGRES_DB")
    DB_ECHO_LOG: bool = False

    @property
    def database_url(self) -> Optional[PostgresDsn]:
        return (
            f"postgresql+asyncpg://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@"
            f"{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}"
        )

    REDIS_HOST: str = os.environ.get("REDIS_HOST")
    REDIS_PORT: int = int(os.environ.get("REDIS_PORT"))
    REDIS_PASSWORD: str = os.environ.get("REDIS_PASSWORD")
    REDIS_DATABASE: int = int(os.environ.get("REDIS_DATABASE"))

    REDIS_TIMEOUT: int = 5
    TOKEN_REDIS_PREFIX: str = "ce_token"
    TOKEN_REFRESH_REDIS_PREFIX: str = "ce_refresh_token"

    CAPTCHA_LOGIN_REDIS_PREFIX: str = "ce_login_captcha"
    CAPTCHA_LOGIN_EXPIRE_SECONDS: int = 60 * 20


@lru_cache
def get_proj_settings():
    return Settings()


settings = get_proj_settings()
