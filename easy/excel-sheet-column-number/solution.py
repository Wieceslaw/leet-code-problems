def titleToNumber(columnTitle: str) -> int:
    result = 0
    for i, el in enumerate(columnTitle[::-1]):
        result += (26 ** i) * (ord(el) - 64)
    return result
