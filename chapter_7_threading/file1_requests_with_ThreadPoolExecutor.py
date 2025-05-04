import time
import requests
from concurrent.futures import ThreadPoolExecutor



def get_example_status(url: str) -> int:
    response = requests.get(url)
    return response.status_code


def main():
    # Многопоточная версия: выполняем 1000 http запросов
    start = time.time()

    with ThreadPoolExecutor() as pool:
        urls = ["https://example.com" for i in range(100)]
        results = pool.map(get_example_status, urls)
        for result in results:
            res = result

        end = time.time()
    
    print(f"(multithread) time elapsed: {end - start}s")

    # Последовательная версия: выполняем 1000 http запросов
    start = time.time()
    urls = ["https://example.com" for i in range(100)]
    for url in urls:
        res = get_example_status(url)
    end = time.time()
    
    print(f"(syncronious) time elapsed: {end - start}s")


if __name__ == "__main__":
    main()
    main()