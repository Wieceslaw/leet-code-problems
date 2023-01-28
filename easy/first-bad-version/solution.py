def isBadVersion(version: int) -> bool:
    bad = 1150769282
    if version >= bad:
        return True
    return False


def firstBadVersion(n: int) -> int:
    k = n // 2 + 1
    ptr = k
    while k:
        if isBadVersion(ptr):
            ptr -= k
        else:
            ptr += k
        k //= 2
    while not isBadVersion(ptr):
        ptr += 1
    return ptr


print(firstBadVersion(1420736637))
