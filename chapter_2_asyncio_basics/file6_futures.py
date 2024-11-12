import asyncio
from asyncio import Future


async def set_future_value(future: Future) -> None:
    await asyncio.sleep(1)
    future.set_result(42)

async def main():
    my_future = Future()
    asyncio.create_task(set_future_value(my_future))
    print("Будущий объект готов:", my_future.done())

    value = await my_future
    print("Будущий объект готов:", my_future.done())
    print(value)



asyncio.run(main())

