from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.logging import configure_logging, get_logger
from app.core.settings import get_settings
from app.routes import health_router, normalize_router, clinical_intel_router

configure_logging()
logger = get_logger(__name__)
settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    logger.info('Starting clinical-intel-chat | env=%s version=%s', settings.app_env, settings.app_version)
    yield
    logger.info('Shutting down clinical-intel-chat')


def create_app() -> FastAPI:
    app = FastAPI(
        title='clinical-intel-chat',
        description='Clinical intelligence API for normalized, structured disease and therapy lookups.',
        version=settings.app_version,
        docs_url='/docs',
        redoc_url='/redoc',
        openapi_url='/openapi.json',
        lifespan=lifespan,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.allowed_origins,
        allow_credentials=True,
        allow_methods=['*'],
        allow_headers=['*'],
    )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
        logger.exception('Unhandled exception on %s %s', request.method, request.url.path)
        return JSONResponse(status_code=500, content={'detail': 'An unexpected error occurred. Please try again later.'})

    app.include_router(health_router)
    app.include_router(normalize_router)
    app.include_router(clinical_intel_router)
    return app


app = create_app()
