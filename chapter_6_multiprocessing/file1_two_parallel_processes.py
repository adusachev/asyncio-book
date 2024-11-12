import time
from multiprocessing import Process

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

    process_1 = Process(target=count, args=(100_000_000,))  # создать процесс для выполнения функции count
    process_2 = Process(target=count, args=(200_000_000,))

    process_1.start()  # запустить процесс (управление возвращается немедленно)
    process_2.start()

    process_1.join()  # ждать завершения процесса (блокирует выполнение)
    process_2.join()

    end = time.time()
    time_elapsed = end - start
    print(f"Полное время работы {time_elapsed}")
