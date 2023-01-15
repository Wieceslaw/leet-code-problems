from solution import merge

nums1 = [1, 1, 3, 7, 0, 0, 0, 0]
nums2 = [2, 5, 6, 8]

merge(nums1, len(nums1) - len(nums2), nums2, len(nums2))
print(nums1)
