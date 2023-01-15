def removeElement(nums: list[int], val: int) -> int:
    if not nums:
        return 0

    last_i = 0

    for i in range(len(nums)):
        if nums[i] != val:
            nums[last_i] = nums[i]
            last_i += 1

    return last_i
