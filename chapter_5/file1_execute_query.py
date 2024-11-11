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
    
    await connection.execute("INSERT INTO brand(brand_name) VALUES ('Levis'), ('Seven')")

    query = "SELECT brand_id, brand_name FROM brand"
    results = await connection.fetch(query)  # type(results) = List[asyncpg.Record]

    for row in results:
        print(f"id: {row['brand_id']}, name: {row['brand_name']}")
    
    await connection.close()

asyncio.run(main())
