def missingNumber(nums: list[int]) -> int:
    # nums.sort()
    # if nums[0] > 0:
    #     return 0
    # for i in range(1, len(nums)):
    #     if nums[i - 1] + 1 != nums[i]:
    #         return nums[i] - 1
    # return nums[-1] + 1
    mx = max(nums)
    st = set(range(0, mx + 1))
    for el in nums:
        st.remove(el)
    if len(st) == 0:
        return mx + 1
    return st.pop()



print(missingNumber([1]))
