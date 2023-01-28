def findDisappearedNumbers(nums: list[int]) -> list[int]:
    st = set(nums)
    result = set(range(1, len(nums) + 1))
    return list(result.difference(st))
