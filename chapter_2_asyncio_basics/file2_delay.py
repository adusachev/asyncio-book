import asyncio
from util import delay


async def add_one(number: int) -> int:
    return number + 1

async def hello() -> str:
    await delay(2)
    return "hello"


async def main():
    message = await hello()
    value = await add_one(1)
    print(value)
    print(message)


asyncio.run(main())
