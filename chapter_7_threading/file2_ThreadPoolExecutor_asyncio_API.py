import requests
from concurrent.futures import ThreadPoolExecutor
from util import async_timed
import asyncio
from functools import partial


def get_example_status(url: str) -> int:
    response = requests.get(url)
    return response.status_code


@async_timed
async def main():

    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        urls = ["https://example.com" for i in range(100)]

        tasks = [
            loop.run_in_executor(pool, partial(get_example_status, url)) for url in urls
        ]

        results = await asyncio.gather(*tasks)
        print(len(results), results[0])
    


if __name__ == "__main__":
    asyncio.run(main())