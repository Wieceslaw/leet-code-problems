def searchInsert(nums: list[int], target: int) -> int:
    if not nums:
        return 0

    length = len(nums)
    for i in range(length):
        if nums[i] > target:
            return i
        if nums[i] == target:
            return i
        if i == length - 1:
            return length
        if nums[i] < target < nums[i + 1]:
            return i + 1
