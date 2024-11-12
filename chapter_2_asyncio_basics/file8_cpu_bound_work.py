import asyncio
from util import delay, async_timed

@async_timed
async def cpu_bound_work():
    counter = 0
    for i in range(200000000):  # ~3 sec
        counter = counter + 1
    return counter

@async_timed
async def main():
    task_cpu = asyncio.create_task(cpu_bound_work())
    # здесь возникнет блокировка <----------
    task_io = asyncio.create_task(delay(3))

    await task_cpu
    await task_io

# @async_timed
# async def main():
#     task_io = asyncio.create_task(delay(3))
#     task_cpu = asyncio.create_task(cpu_bound_work())
#     # здесь возникнет блокировка <----------

#     await task_cpu
#     await task_io

asyncio.run(main())