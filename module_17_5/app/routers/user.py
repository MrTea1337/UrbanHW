from fastapi import APIRouter, Depends, status, HTTPException, Query
from sqlalchemy.orm import Session
from module_17_5.app.backend.db_depends import get_db
from typing import Annotated
from  module_17_5.app.models import User, Task
from  module_17_5.app.schemas import CreateUser, UpdateUser
from sqlalchemy import insert, select, update, delete
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    return db.scalars(select(User)).all()

@router.get('/get_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)],
                     user_id: int = Query(ge=1, le=100, description='Enter User ID')):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], create_user: CreateUser):

    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED,
            'transaction': 'Successful'}

@router.put('/update')
async def update_user(db: Annotated[Session, Depends(get_db)],
                     user_id: Annotated[int, Query(ge=1, le=100, description='Enter User ID')],
                     update_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(update(User).where(User.id == user_id).values(
            firstname=update_user.firstname,
            lastname=update_user.lastname,
            age=update_user.age
        ))
        db.commit()
        return {'status_code': status.HTTP_200_OK,
                'transaction': 'User update is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)],
                      user_id: Annotated[int, Query(ge=1, le=100, description='Enter User ID')]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(delete(Task).where(Task.user_id == user_id))
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK,
                'transaction': 'User delete is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')

@router.get('/user_id/tasks')
async def task_by_user_id(db: Annotated[Session, Depends(get_db)],
                          user_id: Annotated[int, Query(ge=1, le=100, description='Enter User ID')]):
    tasks =  db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if tasks:
        return tasks
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Tasks or user was not found')