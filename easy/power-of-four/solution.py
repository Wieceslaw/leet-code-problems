def isPowerOfFour(n: int) -> bool:
    if n <= 0:
        return False
    string = bin(n)
    length = len(string)
    if (length - 3) % 2 != 0:
        return False
    for i in range(3, length):
        if string[i] != '0':
            return False
    return True
