from sanic import Blueprint, response
from sanic.request import Request
from src.controllers.message import MessageController
from src.controllers.authorization import app_authorization

message = Blueprint('content_message', url_prefix='/message')


@message.middleware('request')
async def middleware(request: Request):
    pass


@message.get('/<uid>')
@app_authorization()
async def index(request: Request, uid):
    return await MessageController.index(request, uid)

@message.post('/')
@app_authorization()
async def store(request: Request):
    return await MessageController.store(request)
