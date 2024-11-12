from multiprocessing import Pool
import time


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
    start = time.time()

    with Pool() as process_pool:
        result_1 = process_pool.apply_async(count, args=(100_000_000,))
        result_2 = process_pool.apply_async(count, args=(200_000_000,))
        print(result_1.get())  # blocking
        print(result_2.get())
        # result_1 = process_pool.apply(count, args=(100_000_000,))  # blocking
        # result_2 = process_pool.apply(count, args=(200_000_000,))
        # print(result_1)
        # print(result_2)

    end = time.time()
    time_elapsed = end - start
    print(f"Общее время работы: {time_elapsed} сек")

