import numpy as np
from util import async_timed
from concurrent.futures import ThreadPoolExecutor
import asyncio
from functools import partial



# Создадим большую матрицу и отсортируем ее значения по колонкам
num_rows = 50
num_columns = 10_000_000
# num_rows = 3
# num_columns = 5
matrix = np.random.randint(low=0, high=100, size=(num_rows, num_columns))
print(matrix)
print()


def sort_column(column_values: np.ndarray) -> np.ndarray:
    return np.sort(column_values)


@async_timed
async def main():
    
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        tasks = [
            loop.run_in_executor(pool, partial(sort_column, matrix[i])) for i in range(num_rows)
        ]

    res = await asyncio.gather(*tasks)
    res = np.array(res)
    print(res)


if __name__ == "__main__":
    asyncio.run(main())
