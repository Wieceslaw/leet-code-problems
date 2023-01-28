def countBits(n: int) -> list[int]:
    result = [0, 1]
    if n <= 1:
        return result[:n + 1]

    k = 1
    c = 1
    d = 2
    for i in range(2, n + 1):
        result.append(result[c - 1] + 1)
        if c == d:
            k += 1
            d = 2 ** k
            c = 0
        c += 1
    return result


for i in range(17):
    print(i, ':', countBits(i))
