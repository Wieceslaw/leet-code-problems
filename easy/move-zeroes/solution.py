def moveZeroes(nums: list[int]) -> None:
    start_ptr = None
    end_ptr = None

    for i in range(len(nums)):
        if start_ptr is None and nums[i] == 0:
            start_ptr = i
            end_ptr = start_ptr
        elif start_ptr is not None:
            if nums[i] != 0:
                nums[start_ptr], nums[i] = nums[i], nums[start_ptr]
                start_ptr += 1
            end_ptr += 1


array = [0]
moveZeroes(array)
print(array)
