def isPerfectSquare(num: int) -> bool:
    if num == 1:
        return True
    if num < 4:
        return False
    c = num % 10
    if c in [2, 3, 7, 8]:
        return False

    l = 1
    r = num
    mid = (l + r) // 2

    while l <= r:
        sq = mid * mid
        if sq == num:
            return True
        elif sq < num:
            l = mid + 1
        else:
            r = mid - 1
        mid = (l + r) // 2
    return False


for i in range(1, 145):
    print(i, ':', isPerfectSquare(i))

# print(isPerfectSquare(4))

