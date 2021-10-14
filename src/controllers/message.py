import json

from sanic.request import Request
from sanic import response
from src.models import User, Message
from src.utils.serialize import Serialize


class MessageController:
    @staticmethod
    async def index(request: Request, uid: str):
        page = 1
        size = 5
        sizes = [5, 10, 20]

        uida = request.headers['user']
        user_a = User.get(id=uida)
        user_b = User.get_or_none(id=uid)

        if user_b is None:
            return response.json({'user' f'user {uid} not found'}, status=404)

        if 'page' in request.args:
            _page: str = request.args['page'][0]
            if not _page.isnumeric():
                return response.json({'pages': 'arguments page must be numeric'}, status=400)

            page: int = int(_page)

        if 'size' in request.args:
            _size: str = request.args['size'][0]

            if not _size.isnumeric():
                return response.json({'size': 'argument size must be numeric'}, status=400)

            _size: int = int(_size)
            if _size in sizes:
                size = _size

        messages =  []
        query = Message.select().where(
            (Message.user_a == user_a.id) | (Message.user_b == user_b.id) &
            (Message.user_a == user_b.id) | (Message.user_b == user_a.id)
        )
        count = query.count()
        query = query.paginate(page=page, paginate_by=size)
        pages = count // size
        pages = page + 1 if (count % size) > 0 else page

        for data in query:
            messages.append(data.json)

        data = dict()
        data['pages'] = pages
        data['messages'] = messages

        return response.json(data, dumps=json.dumps, cls=Serialize)


    @staticmethod
    async def store(request: Request):
        uid = request.headers['user']
        user = User.get(id=uid)

        data = request.json.copy()
        data['user_a'] = user.id

        errors = Message.validate(**data)
        if bool(errors):
            return response.json(errors, status=400)


        message = Message.create(**data)


        return response.json(message.json, status=201, dumps=json.dumps, cls=Serialize)


