import asyncio
import time
from typing import Callable, Any
import functools


def async_timed(func: Callable) -> Callable:
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        print(f"Старт функции {func.__name__}")
        start = time.time()
        try:
            result = await func(*args, **kwargs)
            return result
        finally:
            end = time.time()
            time_elapsed = end - start
            print(f"Функция {func.__name__} выполнилась за {time_elapsed} сек")

    return wrapper



#  def async_timed():
#     def wrapper(func: Callable) -> Callable:
#         @functools.wraps(func)
#         async def wrapped(*args, **kwargs) -> Any:
#             print(f'выполняется {func} с аргументами {args} {kwargs}')
#             start = time.time()
#             try:
#                 return await func(*args, **kwargs)
#             finally:
#                 end = time.time()
#                 total = end - start
#                 print(f'{func} завершилась за {total:.4f} с')
#         return wrapped
#     return wrapper