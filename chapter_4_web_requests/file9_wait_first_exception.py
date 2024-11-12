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
        tasks = [
            asyncio.create_task(fetch_status_delay(session, "https://example.com", 1)),
            asyncio.create_task(fetch_status_delay(session, "https://example.com", 1)),
            asyncio.create_task(fetch_status_delay(session, "hty://абырвалг.com", 3)),  # bad request
            asyncio.create_task(fetch_status_delay(session, "https://example.com", 10)),
            asyncio.create_task(fetch_status_delay(session, "https://example.com", 10))
        ]

        finished, pending = await asyncio.wait(tasks, return_when=asyncio.FIRST_EXCEPTION)

        print(f'Число завершившихся задач: {len(finished)}')
        print(f'Число ожидающих задач: {len(pending)}')

        for finished_task in finished:
            if finished_task.exception() is None:
                print(finished_task.result())
            else:
                logging.error("При выполнении запроса возникло исключение",
                              exc_info=finished_task.exception())

        for pending_task in pending:
            pending_task.cancel()

asyncio.run(main())
