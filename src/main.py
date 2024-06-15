from src.database.connection import finish_db, init_db
from src.config.settings import settings
from src.middleware.handler import define_error_handlers
from src.routes import define_routes
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


def get_application() -> FastAPI:
    _app = FastAPI(
        title=settings.PROJECT_NAME,
        docs_url="/docs",
        on_startup=[init_db],
        on_shutdown=[finish_db],
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
define_error_handlers(app)
define_routes(app)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.")
