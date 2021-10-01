from sanic import Blueprint
from .user import user


routes = Blueprint.group([user], url_prefix='/app')