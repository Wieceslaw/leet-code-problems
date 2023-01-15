def maxProfit(prices: list[int]) -> int:
    mn = prices[0]
    max_diff = 0
    for i in range(len(prices)):
        mn = min(mn, prices[i])
        max_diff = max(max_diff, prices[i] - mn)
    return max_diff


print(maxProfit([7, 1, 5, 3, 6, 4]))
