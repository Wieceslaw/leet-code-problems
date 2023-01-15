import math


def getRow(row_index: int) -> list[int]:
    array = [0] * row_index
    for k in range(row_index):
        array[k] = math.factorial(row_index) // (math.factorial(row_index - k) * math.factorial(k))
    return array
