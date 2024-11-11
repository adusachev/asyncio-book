import asyncio
import aiohttp
from aiohttp import ClientSession
from util import async_timed
import logging


@async_timed
async def fetch_status(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status
    

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
        tasks = [
            asyncio.create_task(fetch_status(session, "https://example.com")),
            asyncio.create_task(fetch_status(session, "https://example.com:989"))
        ]
        # tasks = [
        #     asyncio.create_task(fetch_status_delay(session, "https://example.com", 10)),
        #     asyncio.create_task(fetch_status_delay(session, "https://example.com", 1))
        # ]
        finished, pending = await asyncio.wait(tasks)

        print(f'Число завершившихся задач: {len(finished)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for finished_task in finished:
            if finished_task.exception() is None:
                print(finished_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение",
                              exc_info=finished_task.exception())

        # for finished_task in finished:
        #     result = await finished_task
        #     print(result)

asyncio.run(main())
