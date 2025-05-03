import time
from concurrent.futures import ProcessPoolExecutor
import asyncio
from asyncio.events import AbstractEventLoop
from functools import partial


def count(num: int) -> int:
    start = time.time()
    counter = 0
    for i in range(num):
        counter += 1
    end = time.time()
    time_elapsed = end - start
    print(f"Закончен подсчет до {num} за время {time_elapsed} сек")
    return counter


async def main():
    with ProcessPoolExecutor() as process_pool:
        loop: AbstractEventLoop = asyncio.get_running_loop()
        numbers = [100_000_000, 1, 100_000_000, 3, 50]
        calls: list[partial[int]] = [partial(count, num) for num in numbers]

        call_coroutines = []
        for call in calls:
            call_coroutines.append(
                loop.run_in_executor(process_pool, call)
            )
        
        results = await asyncio.gather(*call_coroutines)
        for res in results:
            print(res)

        # for finished_call in asyncio.as_completed(call_coroutines):
        #     print(await finished_call)


if __name__ == "__main__":
    asyncio.run(main())