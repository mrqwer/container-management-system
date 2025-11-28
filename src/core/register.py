from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.config.settings import settings
from src.api.routers import v1
from src.database.postgres import create_table, close_pooled_connections


@asynccontextmanager
async def register_init(app: FastAPI):
    await create_table()
    yield
    await close_pooled_connections()


def register_app() -> FastAPI:
    app = FastAPI(
        title=settings.TITLE,
        version=settings.VERSION,
        description=settings.DESCRIPTION,
        openapi_prefix=settings.OPENAPI_PREFIX,
        docs_url=settings.DOCS_URL,
        openapi_url=settings.OPENAPI_URL,
        lifespan=register_init,
    )
    register_middleware(app)
    register_router(app)
    return app


def register_middleware(app: FastAPI):
    if settings.MIDDLEWARE_CORS:
        from fastapi.middleware.cors import CORSMiddleware

        app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )


def register_router(app: FastAPI):
    app.include_router(v1)
