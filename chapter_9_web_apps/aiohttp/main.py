import asyncpg
from aiohttp import web
from aiohttp.web_app import Application
from aiohttp.web_request import Request
from aiohttp.web_response import Response
from database import create_database_pool, destroy_database_pool, DB_KEY
from asyncpg.pool import Pool
from asyncpg import Record

routes = web.RouteTableDef()



@routes.get('/brands')
async def brands(request: Request) -> Response:
    connection: Pool = request.app[DB_KEY]
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: list[Record] = await connection.fetch(brand_query)
    result_as_dict: list[dict] = [dict(brand) for brand in results]
    print("GET /brands")
    return web.json_response(result_as_dict)



app = web.Application()
app.on_startup.append(create_database_pool)
app.on_cleanup.append(destroy_database_pool)
app.add_routes(routes)
web.run_app(app)
