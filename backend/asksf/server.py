# import logging

# import sentry_sdk
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
# from fastapi.middleware.gzip import GZipMiddleware
# from fastapi.responses import FileResponse
# from fastapi.staticfiles import StaticFiles
# from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
# from starlette.middleware.sessions import SessionMiddleware

from asksf.routes import execute

# from pandanbls.routes import (
#     admin,
#     automation,
#     deploy,
#     execute,
#     settings,
#     user,
#     webhooks,
#     workflow,
# )
# from pandanbls.utils.auth_utils import get_sentry_dsn
# from pandanbls.utils.aws_utils import get_secret
# from pandanbls.utils.settings import Environment
# from pandanbls.utils.settings import settings as pandan_settings
# from pandanbls.utils.settings import setup_logging

# setup_logging()
# logger = logging.getLogger(__name__)


# def _get_server_secret_key() -> str:
#     secret = get_secret("pandanai/serversecretkey")
#     return secret["secret_key"]


# server_secret_key = _get_server_secret_key()


app = FastAPI()
# app.include_router(user.router)
# app.include_router(deploy.router)
app.include_router(execute.router)
# app.include_router(workflow.router)
# app.include_router(settings.router)
# app.include_router(automation.router)
# app.include_router(webhooks.router)
# app.include_router(admin.router)

# app.add_middleware(SessionMiddleware, secret_key=server_secret_key)
# app.add_middleware(GZipMiddleware, minimum_size=1000)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# if pandan_settings.environment != Environment.dev:
#     sentry_dsn = get_sentry_dsn()
#     sentry_sdk.init(
#         sentry_dsn, traces_sample_rate=0.05, profiles_sample_rate=1.0
#     )
#     app.add_middleware(SentryAsgiMiddleware)

#     @app.get("/")
#     @app.get("/settings")
#     @app.get("/admin")
#     @app.get("/email-not-verified")
#     @app.get("/automation/{automation_id}")
#     async def index():
#         return FileResponse("./pandanbls/ui/index.html")

#     @app.get("/healthz")
#     async def healthz():
#         return {"status": "ok"}

#     app.mount("/", StaticFiles(directory="./pandanbls/ui/"), name="ui")
