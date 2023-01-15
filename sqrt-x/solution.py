def mySqrt(x: int) -> int:
    # TODO:
    if x == 0 or x == 1:
        return x
    result = 0
    for i in range(x + 1):
        if i * i > x:
            result = i
            break
    if result * result > x:
        result -= 1
    return result
