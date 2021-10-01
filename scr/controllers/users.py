from sanic.request import Request
from sanic import response

class UserCoontroller:
    @staticmethod
    async def index(request: Request):
        pass

    @staticmethod
    async def show(request: Request, uid: str):
        pass

    @staticmethod
    async def store(request: Request):
        pass

    @staticmethod
    async def destroy(request: Request, uid: str):
        pass

    @staticmethod
    async def update(request: Request, uid: str):
        pass



