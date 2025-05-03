import time

freqs = dict()

data_path = "/home/usacheval/asyncio_book/chapter_6_multiprocessing/data/googlebooks-eng-all-1gram-20120701-a"

with open(data_path, "r") as f:
    lines = f.readlines()
    print(len(lines))

    start = time.time()
    for line in lines:
        data = line.split("\t")
        
        word = data[0]
        count = int(data[2])
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1

end = time.time()
print(f"Time elapsed: {end - start}")