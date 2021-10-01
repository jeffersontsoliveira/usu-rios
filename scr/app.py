from sanic import Sanic
from sanic.request import Request
from sanic import response
from .routes import routes

app = Sanic(__name__)
app.blueprints(routes)



@app.listener('before_server_start')
async def creat_tables(Server: Sanic, _):
    print('Antes  do servidor iniciar')


@app.listener('after_server_start')
async def depois(server: Sanic, _):
    print('depois do server iniciar')



