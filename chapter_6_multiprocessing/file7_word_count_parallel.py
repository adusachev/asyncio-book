import time
from typing import Iterator, Any
from asyncio import AbstractEventLoop
import asyncio
from concurrent.futures import ProcessPoolExecutor
from functools import partial
import functools


def partition(
    data: list[Any],
    chunk_size: int,
) -> Iterator[list[Any]]:
    for i in range(0, len(data), chunk_size):
        yield data[i : i + chunk_size]


def map_frequencies(chunk: list[str]) -> dict[str, int]:
    freqs = dict()
    for line in chunk:
        word, _, count, _ = line.split("\t")
        if word in freqs:
            freqs[word] += int(count)
        else:
            freqs[word] = int(count)
    
    return freqs


def merge_dictionaries(
    first: dict[str, int],
    second: dict[str, int],
) -> dict[str, int]:
    merged_dict = first
    for key in second:
        if key in first:
            merged_dict[key] += second[key]
        else:
            merged_dict[key] = second[key]
    
    return merged_dict



async def main(partition_size: int):

    data_path = "/home/usacheval/asyncio_book/chapter_6_multiprocessing/data/googlebooks-eng-all-1gram-20120701-a"

    with open(data_path, "r") as f:
        lines = f.readlines()
        loop: AbstractEventLoop = asyncio.get_running_loop()
        tasks = []

        start = time.time()

        with ProcessPoolExecutor() as process_pool:
            for chunk in partition(lines, partition_size):
                task = loop.run_in_executor(
                    process_pool,
                    partial(map_frequencies, chunk)
                )
                tasks.append(task)
            
            intermediate_results = await asyncio.gather(*tasks)

            # Объединение результатов
            final_result = functools.reduce(merge_dictionaries, intermediate_results)
            print(f"Aardvark встречается {final_result['Aardvark']} раз.")

        end = time.time()
        print(f"Time elapsed: {end - start}")


if __name__ == "__main__":
    asyncio.run(main(partition_size=100_000))
