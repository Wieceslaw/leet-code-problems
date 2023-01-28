def thirdMax(nums: list[int]) -> int:
    st = set(nums)
    if len(st) < 3:
        return max(nums)
    return sorted(list(st))[-3]


nums = [1, 1, 2]
print(thirdMax(nums))
