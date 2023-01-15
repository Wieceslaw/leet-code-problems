def plusOne(digits: list[int]) -> list[int]:
    if not digits:
        return []

    length = len(digits)
    array = digits[::]

    cur = length - 1
    sm = (array[cur] + 1) // 10
    array[cur] = (array[cur] + 1) % 10

    while sm and cur:
        cur -= 1
        temp = sm
        sm = (array[cur] + temp) // 10
        array[cur] = (array[cur] + temp) % 10

    if sm and not cur:
        return [sm] + array

    return array
