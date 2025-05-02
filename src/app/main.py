from fastapi import FastAPI

from src.app.users.router import router as users_router
from src.app.projects.router import router as projects_router
from src.app.tasks.router import router as tasks_router

app = FastAPI()

app.include_router(users_router)
app.include_router(projects_router)
app.include_router(tasks_router)

@app.get("/info")
async def get_info():
    return "Hello, miltitasker!"