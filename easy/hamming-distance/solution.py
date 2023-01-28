def hammingDistance(x: int, y: int) -> int:
    r = x ^ y
    c = 0
    while r:
        c += (r & 1)
        r >>= 1
    return c


print(hammingDistance(4, 1))
