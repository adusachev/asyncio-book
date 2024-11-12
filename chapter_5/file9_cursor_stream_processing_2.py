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
        cursor = await connection.cursor(query)  # создать крсор для запроса
        await cursor.forward(500)  # сдвинуть курсор на 500 записей вперед
        products = await cursor.fetch(100)  # получить следующие 100 записей
        for product in products:
            print(product)

    await connection.close()


asyncio.run(main())