from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session
from module_17_5.app.backend.db_depends import get_db
from typing import Annotated
from  module_17_5.app.models import Task, User
from  module_17_5.app.schemas import CreateTask, UpdateTask
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])

@router.get('/')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    return db.scalars(select(Task)).all()

@router.get('/task_id')
async def task_by_id(db: Annotated[Session, Depends(get_db)],
                     task_id : int = Query(ge=1, le=100, deskription="Enter Task ID")
                     ):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is not None:
        return task
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Task was not found")

@router.post('/create')
async def create_task(db: Annotated[Session, Depends(get_db)],
                      create_task: CreateTask,
                      user_id: Annotated[int, Query(ge=1, le=100, description='Enter User ID')]):
    user = db.scalar(select(User).where(User.id == user_id))
    if  user is not None:
        db.execute(insert(Task).values(
            title=create_task.title,
            content=create_task.content,
            priority=create_task.priority,
            slug=slugify(create_task.title),
            user_id=user_id
        ))
        db.commit()
        return {'status_code': status.HTTP_201_CREATED,
                'transaction': 'Successful'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="User was not found")

@router.put('/update')
async def update_task(db: Annotated[Session, Depends(get_db)],
                      task_id: Annotated[int, Query(ge=1, le=100, description='Enter Task ID')],
                      update_task : UpdateTask):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is not None:
        db.execute(update(Task).where(Task.id == task_id)).values(
            title=update_task.title,
            content=update_task.content,
            priority=update_task.priority,
            slug=slugify(update_task.title)
        )
        db.commit()
        return {'status_code' : status.HTTP_200_OK,
                'transaction': 'Task update is successful!'}

@router.delete('/delete')
async def delete_task(db: Annotated[Session, Depends(get_db)],
                      task_id: Annotated[int, Query(ge=1, le=100, description='Enter Task ID')]):
    task = db.scalar(select(Task).where(Task.id == task_id))
    if task is not None:
        db.execute(delete(Task).where(Task.id == task_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK,
                'transaction': 'Task delete is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')