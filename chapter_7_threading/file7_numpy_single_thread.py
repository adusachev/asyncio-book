import numpy as np
import time


# Создадим большую матрицу и отсортируем ее значения по колонкам
num_rows = 50
num_columns = 10_000_000
# num_rows = 3
# num_columns = 5

matrix = np.random.randint(low=0, high=100, size=(num_rows, num_columns))
print(matrix)
print()

start = time.time()

res = np.sort(matrix, axis=1)
print(res)

end = time.time()

print(f"Time elapsed: {end - start}")