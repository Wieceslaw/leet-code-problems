def char_xor(char_a, char_b):
    if char_a == '1' and char_b == '0':
        return '1'
    if char_b == '1' and char_a == '0':
        return '1'
    return '0'


def char_and(char_a, char_b):
    if char_a == '1' and char_b == '1':
        return '1'
    return '0'


def addBinary(a: str, b: str) -> str:
    a_len = len(a)
    b_len = len(b)
    min_len = min(a_len, b_len)
    max_len = max(a_len, b_len)

    result = ['0'] * max_len

    cur = 0
    sm = '1'

    while cur != -min_len and sm == '1':
        cur -= 1
        sm = char_and(a[cur], b[cur])
        result[cur] = char_xor(a[cur], b[cur])

    if cur == -min_len and sm == '1':
        return ''.join(['1'] + result)
    return ''.join(result)
