def climbStairs(n: int) -> int:
    if n == 0:
        return 1

    array = [0] * (n + 1)
    array[0] = 1
    for i in range(1, n + 1):
        if i - 1 >= 0:
            array[i] += array[i - 1]
        if i - 2 >= 0:
            array[i] += array[i - 2]

    return array[-1]
