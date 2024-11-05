import asyncio
from util import delay


async def main():
    task = asyncio.create_task(delay(2))
    try:
        result = await asyncio.wait_for(task, timeout=1)
        print(result)
    except TimeoutError:
        print("Превышен лимит ожидания")


asyncio.run(main())