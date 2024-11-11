import asyncpg
import asyncio
from typing import List, Tuple, Union
from random import sample


def load_common_words() -> List[str]:
    with open('./chapter_5/common_words.txt') as common_words:
        words = common_words.readlines()
        
    for i, word in enumerate(words):
        if word.endswith("\n"):
            words[i] = word[:-1]
    return words


def generate_brand_names(words: List[str]) -> List[Tuple[Union[str, ]]]:
    return [(words[index],) for index in sample(range(100), 100)]


async def insert_brands(common_words, connection) -> int:
    brands = generate_brand_names(common_words)
    insert_brands = "INSERT INTO brand VALUES(DEFAULT, $1)"
    return await connection.executemany(insert_brands, brands)


async def main():
    common_words = load_common_words()

    connection = await asyncpg.connect(
        host='127.0.0.1', 
        port=5432,
        user='aleksei',
        database='mydb',
        password='pass'
    )
    await insert_brands(common_words, connection)


asyncio.run(main())
