import asyncio
from util import delay


async def get_numbers(n: int):
    for i in range(n):
        await delay(1)
        yield i


async def main():
    generator_async = get_numbers(5)

    async for elem in generator_async:
        print(elem)


asyncio.run(main())
