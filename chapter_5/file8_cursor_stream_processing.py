import asyncpg
import asyncio

db_settings = {
    "host": "127.0.0.1",
    "port": 5432,
    "user": "aleksei",
    "database": "mydb",
    "password": "pass"
}


async def main():
    connection = await asyncpg.connect(**db_settings)

    async with connection.transaction():
        query = "SELECT product_id, product_name FROM product"
        async for product in connection.cursor(query):
            print(product)
    
    await connection.close()


asyncio.run(main())