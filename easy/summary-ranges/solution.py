def summaryRanges(nums: list[int]) -> list[str]:
    result = []
    current = []
    length = len(nums)
    if length == 1:
        return [str(nums[0])]
    for i, num in enumerate(nums):
        if i == 0:
            current.append(num)
        else:
            if num - nums[i - 1] != 1:
                current.append(nums[i - 1])
                if current[0] == current[1]:
                    result.append(str(current[0]))
                else:
                    result.append(f"{current[0]}->{current[1]}")
                current = [num]
            if i == length - 1:
                current.append(num)
                if current[0] == current[1]:
                    result.append(str(current[0]))
                else:
                    result.append(f"{current[0]}->{current[1]}")
    return result


print(summaryRanges([0, 2, 3, 4, 6, 8, 9]))
