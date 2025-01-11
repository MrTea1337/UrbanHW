from fastapi import FastAPI
from module_17_4.app.routers import task, user
import logging
from fastapi.logger import logger as fastapi_logger

logging.basicConfig(level=logging.INFO)
fastapi_logger.setLevel(logging.INFO)


app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {"message": "Welcome to Taskmanager"}

app.include_router(user.router)
app.include_router(task.router)