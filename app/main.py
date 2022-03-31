from fastapi import FastAPI

from .users.router import router as users_router
from .auth.router import router as auth_router
from .jobs.router import router as jobs_router
from .db import Base, engine


app = FastAPI()

app.include_router(users_router, prefix="/users")
app.include_router(auth_router, prefix="/auth")
app.include_router(jobs_router, prefix="/jobs")

Base.metadata.create_all(bind=engine)


@app.get("/")
async def is_alive():
    return {"Is alive": "yes"}


