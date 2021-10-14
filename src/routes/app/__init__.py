from sanic import Blueprint
from .user import user
from .message import message

app = Blueprint.group([user, message], url_prefix='/app')


