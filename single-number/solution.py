def singleNumber(nums: list[int]) -> int:
    st = set()
    for num in nums:
        if num in st:
            st.remove(num)
        else:
            st.add(num)
    return st.pop()
