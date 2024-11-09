import asyncio
from util import async_timed, delay

@async_timed
async def main():
    """
    Создает 1000 задач и конкурентно выполняет их
    """
    delay_list = [2] * 1000
    
    tasks = [ asyncio.create_task(delay(seconds_num)) for seconds_num in delay_list ]

    [ await task for task in tasks ]


asyncio.run(main())
