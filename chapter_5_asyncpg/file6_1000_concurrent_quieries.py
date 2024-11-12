import asyncpg
import asyncio
from asyncpg import Record
from typing import List
from util import async_timed

query = \
"""
SELECT
    p.product_id,
    p.product_name,
    p.brand_id,
    s.sku_id,
    pc.product_color_name,
    ps.product_size_name
FROM product as p
    JOIN sku as s on s.product_id = p.product_id
    JOIN product_color as pc on pc.product_color_id = s.product_color_id
    JOIN product_size as ps on ps.product_size_id = s.product_size_id
WHERE p.product_id = 100"""

db_settings = {
    "host": "127.0.0.1",
    "port": 5432,
    "user": "aleksei",
    "database": "mydb",
    "password": "pass",
    "min_size": 6,
    "max_size": 6
}


async def get_product_info(pool):
    async with pool.acquire() as connection:
        result = await connection.fetchrow(query)
        return result


@async_timed
async def concurrent_queries(pool, queries_number):
    queries = [get_product_info(pool) for i in range(queries_number)]
    results = await asyncio.gather(*queries)
    return results


@async_timed
async def synchronous_queries(pool, queries_number):
    results = [await get_product_info(pool) for i in range(queries_number)]  # await each query
    return results


@async_timed
async def main():

    async with asyncpg.create_pool(**db_settings) as pool:
        results_1 = await concurrent_queries(pool, 100000)
        results_2 = await synchronous_queries(pool, 100000)
    
    assert results_1 == results_2


asyncio.run(main())
