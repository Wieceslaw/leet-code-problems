def func(n) -> int:
    result = 0
    while n >= 10:
        result += (n % 10) ** 2
        n //= 10
    result += n ** 2
    return result


def isHappy(n: int) -> bool:
    while n != 1:
        n = func(n)
        print(n)
    return True


print(isHappy(2))
