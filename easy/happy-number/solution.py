def func(n) -> int:
    result = 0
    while n >= 10:
        result += (n % 10) ** 2
        n //= 10
    result += n ** 2
    return result


def isHappy(n: int) -> bool:
    st = {n}
    while n != 1:
        n = func(n)
        if n in st:
            return False
        st.add(n)
    return True


print(isHappy(2))
