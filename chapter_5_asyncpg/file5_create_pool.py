import asyncpg
import asyncio
from asyncpg import Record
from typing import List


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


async def main():

    async with asyncpg.create_pool(**db_settings) as pool:
        results = await asyncio.gather(get_product_info(pool),
                                       get_product_info(pool))
    
    print(results)


asyncio.run(main())
