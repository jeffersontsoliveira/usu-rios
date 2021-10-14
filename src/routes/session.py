from sanic import Blueprint
from sanic.request import Request
from src.controllers.session import SessionController

session = Blueprint('content_session', url_prefix='/session')


@session.post('/')
async def store(request: Request):
    return await SessionController.store(request)