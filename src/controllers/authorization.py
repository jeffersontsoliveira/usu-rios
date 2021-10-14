from functools import wraps
from sanic import response
from src.models import User
from sanic.request import Request

import jwt


def app_authorization():
    def decorator(func):
        @wraps(func)
        async def authorization(request: Request, *args, **kwargs):
            if request.token is None:
                return response.json({'token': 'token not provider'}, status=401)
            token = request.token
            secret = '5ba4919543f7d155c9838c20499e30c7'

            try:
                token_decoded = jwt.decode(
                    token,
                    secret,
                    algorithms=['HS256']
                )

            except jwt.ExpiredSignatureError:
                return response.json({'token': 'token expired'}, status=403)

            except jwt.InvalidTokenError:
                return response.json({'token': 'token invalid'}, status=403)

            uid = token_decoded['user']
            user = User.get_or_none(id=uid)

            if user is None:
                return response.json({'token': 'token invalid'}, status=403)


            request.headers['user'] = user.id

            return await func(request, *args, **kwargs)

            #is_authorized = await check_request_for_authorization_status(request)
            #
            #if is_authorized:
            #    response = await f(request, *args, **kwargs)
            #    return response
            #else:
            #    return json({"status": "not_authorized"}, 403)
        return authorization
    return decorator