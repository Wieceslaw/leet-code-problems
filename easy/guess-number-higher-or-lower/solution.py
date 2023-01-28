def guess(num: int):
    nm = 2
    if num == nm:
        return 0
    if num > nm:
        return -1
    return 1


def guessNumber(n: int) -> int:
    l = 1
    r = n
    while l <= r:
        mid = (l + r) // 2
        gs = guess(mid)
        if gs == 1:
            l = mid + 1
        elif gs == -1:
            r = mid - 1
        else:
            return mid


print(guessNumber(2))
