import hashlib
import os
import string
import random
from util import async_timed
from concurrent.futures import ThreadPoolExecutor
import asyncio
from functools import partial

def random_password(length: int) -> bytes:
    random_pass_symbols = [random.choice(string.ascii_lowercase) for i in range(length)]
    random_pass = "".join(random_pass_symbols)
    return random_pass.encode("utf-8")



def hash(password: bytes) -> str:
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))


@async_timed
async def main():

    passwords = [random_password(10) for i in range(10_000)]
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        tasks = [
            loop.run_in_executor(pool, partial(hash, password)) for password in passwords
        ]

    results = await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())
