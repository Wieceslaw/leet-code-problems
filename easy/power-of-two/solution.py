def isPowerOfTwo(n: int) -> bool:
    return bin(n).count('1') == 1
