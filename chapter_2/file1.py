import asyncio


async def add_one(number: int) -> int:
    return number + 1

res = asyncio.run(add_one(2))

print(res)