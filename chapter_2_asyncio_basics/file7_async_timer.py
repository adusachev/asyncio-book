import asyncio
from util import async_timed, delay


@async_timed
async def main():
    task_1 = asyncio.create_task(delay(2))
    task_2 = asyncio.create_task(delay(2))
    task_3 = asyncio.create_task(delay(2))

    await task_1
    await task_2
    await task_3


asyncio.run(main())
