from sanic import Sanic
from sanic.request import Request
from sanic import response

app = Sanic(__name__)



@app.route('/user', methods=['GET', 'POST', 'PUT', 'DELETE'])
async def user(request: Request):
    return response.text(f'Hello world')



