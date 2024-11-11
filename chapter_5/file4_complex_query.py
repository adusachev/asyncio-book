import asyncpg
import asyncio
from asyncpg import Record
from typing import List


async def main():
    connection = await asyncpg.connect(
        host="127.0.0.1",
        port=5432,
        user="aleksei",
        database="mydb",
        password="pass"
    )

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
    
    queries = [connection.execute(query),
               connection.execute(query)]
    
    results = await asyncio.gather(*queries)
    
    await connection.close()

asyncio.run(main())
