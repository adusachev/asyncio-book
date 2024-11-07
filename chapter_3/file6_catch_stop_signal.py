import asyncio
import signal
from util import delay


def cancel_tasks():
    print("Получен сигнал SIGINT!")
    tasks = asyncio.all_tasks()
    print(f"Снимается {len(tasks)} задач")
    [task.cancel() for task in tasks]

async def main():
    loop = asyncio.get_running_loop()

    loop.add_signal_handler(signal.SIGINT, cancel_tasks)

    task_1 = asyncio.create_task(delay(10))
    task_2 = asyncio.create_task(delay(10))
    
    await task_1
    await task_2


asyncio.run(main())
