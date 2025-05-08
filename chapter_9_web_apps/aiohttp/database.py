import asyncpg
from asyncpg.pool import Pool
from aiohttp.web_app import Application


DB_KEY = 'database'


async def create_database_pool(app: Application) -> None:
    print('Создается пул подключений.')
    pool: Pool = await asyncpg.create_pool(
        host='127.0.0.1',
        port=5432,
        user='aleksei',
        password='pass',
        database='mydb',
        min_size=6,
        max_size=6,
    )
    app[DB_KEY] = pool


async def destroy_database_pool(app: Application) -> None:
    print('Уничтожается пул подключений.')
    pool: Pool = app[DB_KEY]
    pool.close()
