import functools

def map_frequency(text: str) -> dict[str, int]:
    words = text.split(" ")
    frequencies = dict()
    for word in words:
        if word in frequencies:
            frequencies[word] += 1
        else:
            frequencies[word] = 1
    
    return frequencies


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


lines = [
    "I know what I know",
    "I know that I know",
    "I don't know much",
    "They don't know much",
]

frequencies_dicts = [map_frequency(line) for line in lines]

print(functools.reduce(merge_dictionaries, frequencies_dicts))