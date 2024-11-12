import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed

@async_timed
async def fetch_status_delay(
        session: ClientSession,
        url: str,
        delay_seconds: int) -> int:
    await asyncio.sleep(delay_seconds)
    async with session.get(url) as result:
        return result.status
    
@async_timed
async def main():
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_status_delay(session, 'https://www.example.com', 10),
                 fetch_status_delay(session, 'https://www.example.com', 20),
                 fetch_status_delay(session, 'https://www.example.com', 1)]
        
        for finished_task in asyncio.as_completed(tasks, timeout=2):
            try:
                res = await finished_task
                print(res)
            except TimeoutError:
                print("Произошел таймаут")

asyncio.run(main())