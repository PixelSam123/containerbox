from fastapi import FastAPI

from .routers import root

app = FastAPI(
    title="containexec",
    description="Use a Docker host to execute requested code in containers",
)

app.include_router(root.router)
