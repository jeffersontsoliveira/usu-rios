from sanic import Blueprint
from sanic.request import Request
from scr.controllers.users import UserCoontroller

user = Blueprint('content_user', url_prefix='/users')

@user.get('/')
async def index(request: Request):
    return await UserCoontroller.index(request)


@user.get('/<uid>')
async def show(request: Request, uid):
    return await UserCoontroller.show(request, uid)


@user.post('/')
async def store(request: Request):
    return await UserCoontroller.store(request,)


@user.delete('/<uid>')
async def destroy(request: Request, uid):
    return await UserCoontroller.destroy(request, uid)


@yser.put('/<uid>')
async def update(request: Request, uid):
    return await UserCoontroller.update(request, uid)



