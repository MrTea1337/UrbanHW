from fastapi import APIRouter, Depends, status, HTTPException, Query
# Сессия БД
from sqlalchemy.orm import Session
# Функция подключения к БД
from module_17_4.app.backend.db_depends import get_db
# Аннотации, Модели БД и Pydantic.
from typing import Annotated
from  module_17_4.app.models import User
from  module_17_4.app.schemas import CreateUser, UpdateUser
# Функции работы с записями.
from sqlalchemy import insert, select, update, delete, Delete
# Функция создания slug-строки
from slugify import slugify
from typing import cast

router = APIRouter(prefix='/user', tags=['user'])


# Должна возвращать список всех пользователей из БД. Используйте scalars, select и all
@router.get('/')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User)).all()
    return users

# Для извлечения записи используйте ранее импортированную функцию select.
# Дополнительно принимает user_id.
# Выбирает одного пользователя из БД.
# Если пользователь не None, то возвращает его.
# В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
@router.get('/get_id')
async def user_by_id(db: Annotated[Session, Depends(get_db)],
                     user_id: int = Query(ge=1, le=100, description='Enter User ID')):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        return user
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')


# Для извлечения записи используйте ранее импортированную функцию select.
# Дополнительно принимает модель CreateUser.
# Подставляет в таблицу User запись значениями указанными в CreateUser.
# В конце возвращает словарь {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
# Обработку исключения существующего пользователя по user_id или username можете сделать по желанию.
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

# Для обновления используйте ранее импортированную функцию update.
# Дополнительно принимает модель UpdateUser и user_id.
# Если находит пользователя с user_id, то заменяет эту запись значениям из модели UpdateUser. Далее возвращает словарь {'status_code': status.HTTP_200_OK, 'transaction': 'User update is successful!'}
# В противном случае выбрасывает исключение с кодом 404 и описанием "User was not found"
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

# Для удаления используйте ранее импортированную функцию delete.
# Всё должно работать аналогично функции update_user, только объект удаляется.
# Исключение выбрасывать то же.
@router.delete('/delete')
async def delete_user(db: Annotated[Session, Depends(get_db)],
                      user_id: Annotated[int, Query(ge=1, le=100, description='Enter User ID')]):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is not None:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {'status_code': status.HTTP_200_OK,
                'transaction': 'User delete is successful!'}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User was not found')