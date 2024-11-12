import asyncio
from util import delay


async def main():
    sleep_1 = asyncio.create_task(delay(3))
    sleep_2 = asyncio.create_task(delay(3))
    sleep_3 = asyncio.create_task(delay(3))

    print("tasks start here")
    print(sleep_1)
    await sleep_1
    print(1+1)
    await sleep_2
    await sleep_3


asyncio.run(main())
