from fastapi import FastAPI

from src.app.projects.router import router as projects_router

app = FastAPI()

app.include_router(projects_router)

@app.get("/info")
async def get_info():
    return "Hello, miltitasker!"