from sanic import blueprints
from sanic import Request

user = blueprints('content_user', url_prefix='/users')

@user.get('/')
async def index(request: Request):
    pass


@user.get('/<uid>')
async def show(request: Request, uid):
    pass


@user.post('/')
async def store(request: Request):
    pass


@user.delete('/<uid>')
async def destroy(request: Request, uid):
    pass


@yser.put('/<uid>')
async def   update(request: Request, uid):



