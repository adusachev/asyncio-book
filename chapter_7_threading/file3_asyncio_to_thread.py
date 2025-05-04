import requests
from util import async_timed
import asyncio
from functools import partial
import os

def get_example_status(url: str) -> int:
    print(f"[Thread] PID: {os.getpid()}")
    response = requests.get(url)
    return response.status_code

@async_timed
async def main():
    urls = ["https://example.com" for i in range(500)]
    tasks = [asyncio.to_thread(get_example_status, url) for url in urls]

    results = await asyncio.gather(*tasks)
    print(len(results), results[0])

if __name__ == "__main__":
    asyncio.run(main())
