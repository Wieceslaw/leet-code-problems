def generate(numRows: int) -> list[list[int]]:
    result = [[]] * numRows
    for i in range(numRows):
        n = i + 1
        if i == 0:
            cur_row = [1]
        else:
            cur_row = [0] * n
            prev = result[i - 1]
            for j in range(n):
                if j == 0:
                    cur_row[j] = prev[j]
                elif j == n - 1:
                    cur_row[j] = prev[j - 1]
                else:
                    cur_row[j] = prev[j - 1] + prev[j]
        result[i] = cur_row

    return result


print(generate(2))
