from functools import partial
import requests
import asyncio
from concurrent.futures import ThreadPoolExecutor
from util import async_timed

from threading import Lock


counter_lock = Lock()
counter: int = 0  # shared data

def get_status_code(url: str) -> int:
    global counter
    response = requests.get(url)
    with counter_lock:  # критическая секция
        counter = counter + 1
    return response.status_code


async def reporter(requests_count: int):
    while counter < requests_count:
        print(f"Завершено запросов: {counter}/{requests_count}")
        await asyncio.sleep(0.5)


@async_timed
async def main():
    loop = asyncio.get_running_loop()
    with ThreadPoolExecutor() as pool:
        requests_count = 200
        urls = ["https://example.com" for i in range(requests_count)]
        reporter_task = asyncio.create_task(reporter(requests_count))
        tasks = [
            loop.run_in_executor(pool, partial(get_status_code, url)) for url in urls
        ]
        results = await asyncio.gather(*tasks)
        await reporter_task
        print(results)


if __name__ == "__main__":
    asyncio.run(main())
