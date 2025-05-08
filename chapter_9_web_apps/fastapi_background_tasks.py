from fastapi import FastAPI, BackgroundTasks
import asyncio
import time

app = FastAPI()


def sync_task(message: str):
    time.sleep(3)
    print(f"Отправлен email: {message}")

async def async_task():
    await asyncio.sleep(3)
    print("Выполнен запрос в сторонний API")


@app.post("/async_task/")
async def route_with_async_task():

    asyncio.create_task(async_task())
    ...
    return {"data": 1}


@app.post("/sync_task/")
async def route_with_sync_task(
    bg_task: BackgroundTasks
):
    bg_task.add_task(sync_task, message="hello")
    ...
    return {"data": 1}


# how to run: fastapi dev ./chapter_8_web_apps/fastapi_background_tasks.py