def removeDuplicates(nums: list[int]) -> int:
    if not nums:
        return 0

    current_number = nums[0]
    k = 1
    last_i = 1

    for i in range(len(nums)):
        if nums[i] != current_number:
            k += 1
            current_number = nums[i]
            nums[last_i] = current_number
            last_i += 1

    return k
