import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
import logging


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
    async with ClientSession() as session:
        pending = [
            asyncio.create_task(fetch_status_delay(session, "https://example.com", 5)),
            asyncio.create_task(fetch_status_delay(session, "https://example.com", 2)),
            asyncio.create_task(fetch_status_delay(session, "https://example.com", 7))
        ]

        while pending:
            finished, pending = await asyncio.wait(pending, return_when=asyncio.FIRST_COMPLETED)

            print(f'Число завершившихся задач: {len(finished)}')
            print(f'Число ожидающих задач: {len(pending)}')

            for finished_task in finished:
                print(await finished_task)

asyncio.run(main())
