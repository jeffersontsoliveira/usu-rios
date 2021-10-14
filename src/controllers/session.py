import json

from sanic.request import Request
from sanic import response
from src.models.user import User
from datetime import datetime, timedelta
from src.utils.serialize import Serialize

import jwt

class SessionController:
    @staticmethod
    async def store(request: Request):
        email = request.json['email']
        password = request.json['password']

        user = User.get_or_none(email=email)
        if user is None:
            return response.json({'user': 'user not found'}, status=404)

        if user.password != password:
            return response.json({'password': 'password does not match'}, status=403)

        expired =  datetime.utcnow() + timedelta(minutes=30)
        secret = '5ba4919543f7d155c9838c20499e30c7'

        payload ={
            'user': user.id,
            'exp': expired
        }
        token = jwt.encode(payload, secret, algorithm='HS256')

        data = dict()
        data['token'] = token
        data['user'] = user.json

        return response.json(data, dumps=json.dumps, cls=Serialize)