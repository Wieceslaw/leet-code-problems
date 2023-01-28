# O(n^2)
# def twoSum(nums: list[int], target: int) -> list[int]:
#     length = len(nums)
#     for i in range(length):
#         for j in range(i + 1, length):
#             if nums[i] + nums[j] == target:
#                 return [i, j]

def twoSum(nums: list[int], target: int) -> list[int]:
    st = set()
    for i, n in enumerate(nums):
        if target - n in st:
            return [nums.index(target - n), i]
        st.add(n)


print(twoSum([3, 2, 4], 6))
