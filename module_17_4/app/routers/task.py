from fastapi import APIRouter, Depends, status, HTTPException
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from module_17_4.app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from  module_17_4.app.models import Task
from  module_17_4.app.schemas import CreateTask, UpdateTask
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete
# Функция создания slug-строки
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    pass

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)]):
    pass

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)]):
    pass

@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)]):
    pass

@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)]):
    pass