def addDigits(num: int) -> int:
    def func(n: int):
        temp = 0
        while n >= 10:
            temp += n % 10
            n //= 10
        return temp + n

    while num > 9:
        num = func(num)
    return num


print(addDigits(123333))
