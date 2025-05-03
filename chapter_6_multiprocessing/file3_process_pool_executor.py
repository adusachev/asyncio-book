import time
from concurrent.futures import ProcessPoolExecutor


def count(num: int) -> int:
    start = time.time()
    counter = 0
    for i in range(num):
        counter += 1
    end = time.time()
    time_elapsed = end - start
    print(f"Закончен подсчет до {num} за время {time_elapsed} сек")
    return counter

if __name__ == "__main__":
    with ProcessPoolExecutor() as process_pool:
        numbers = [100_000_000, 1, 2, 3, 50]
        for result in process_pool.map(count, numbers):
            print(result)            
