import asyncpg
from asyncpg import Record
from asyncpg.pool import Pool
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import JSONResponse, Response
from starlette.routing import Route
from typing import List, Dict


async def create_database_pool():
    print("Try to connect to DB")
    pool: Pool = await asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='aleksei',
        password='pass',
        database='mydb',
        min_size=6,
        max_size=6,
    )
    app.state.DB = pool
    print("Connected to DB")
 

async def destroy_database_pool():
    pool = app.state.DB
    await pool.close()

async def brands(request: Request) -> Response:
    connection: Pool = request.app.state.DB
    brand_query = 'SELECT brand_id, brand_name FROM brand'
    results: List[Record] = await connection.fetch(brand_query)
    result_as_dict: List[Dict] = [dict(brand) for brand in results]
    print("GET brands")
    return JSONResponse(result_as_dict)


app = Starlette(
    routes=[Route('/brands', brands)],
    on_startup=[create_database_pool],
    on_shutdown=[destroy_database_pool],
)

## Run: with 8 workers
# uvicorn --workers 8 --log-level error main:app
