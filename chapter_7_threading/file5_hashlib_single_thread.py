import hashlib
import os
import string
import random
import time

def random_password(length: int) -> bytes:
    random_pass_symbols = [random.choice(string.ascii_lowercase) for i in range(length)]
    random_pass = "".join(random_pass_symbols)
    return random_pass.encode("utf-8")

passwords = [random_password(10) for i in range(10_000)]

def hash(password: bytes) -> str:
    salt = os.urandom(16)
    return str(hashlib.scrypt(password, salt=salt, n=2048, p=1, r=8))

start = time.time()

for password in passwords:
    hash(password)

end = time.time()

print(f"Time elapsed: {end - start}")
