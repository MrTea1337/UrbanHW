from typing import Annotated
from fastapi import FastAPI, Path, HTTPException, Request
from pydantic import BaseModel
from starlette.responses import HTMLResponse
from starlette.templating import Jinja2Templates

app = FastAPI(swagger_ui_parameters={"tryItOutEnabled": True}, debug=True)
users = []
templates = Jinja2Templates(directory='templates')


class User(BaseModel):
    id: int
    username: str
    age: int
FastAPI(debug=True)

@app.get('/', response_class=HTMLResponse)
async def get_main_page(request: Request):
    return templates.TemplateResponse('users.html', {'request': request, 'users': users})

@app.get('/users/{user_id}', response_class=HTMLResponse)
async def get_users(request: Request,
                    user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]):
    try:
        user = next((user for user in users if user.id == user_id))
        return templates.TemplateResponse('users.html', {'request': request, 'user': user})
    except StopIteration:
        raise HTTPException(status_code=404, detail='User not found')

@app.post('/user/{username}/{age}')
async def post_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')], user: User
) -> User:
    if not users:
        user.id = 1
    else:
        user.id = users[-1].id + 1
    user.username = username
    user.age = age
    users.append(user)
    return user

@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
        username: Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')],
        age: Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')],
        user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> User:
    try:
        edit_user = next((user for user in users if user.id == user_id))
        edit_user.username = username
        edit_user.age = age
        return edit_user
    except StopIteration:
        raise HTTPException(status_code=404, detail='User was not found')

@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]) -> User:
    try:
        deleted_user = next((user for user in users if user.id == user_id))
        users.remove(deleted_user)
        return deleted_user
    except StopIteration:
        raise HTTPException(status_code=404, detail='User was not found')
