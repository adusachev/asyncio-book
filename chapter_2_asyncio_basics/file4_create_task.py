import asyncio
from util import delay


async def other_task():
    for i in range(2):
        await asyncio.sleep(1)
        print("Пока остальные спят, я работаю")

    ## блокирует выполнение !!!
    # print("Пока остальные спят, я работаю")
    # result = sum(range(1, 300000000))
    # print(result)

async def main():
    sleep_1 = asyncio.create_task(delay(3))
    sleep_2 = asyncio.create_task(delay(3))
    
    await other_task()
    await sleep_1
    await sleep_2
    


asyncio.run(main())


# import time

# start = time.time()

# a = sum(range(1, 400000000))

# end = time.time()

# print(end - start)
# print(a)