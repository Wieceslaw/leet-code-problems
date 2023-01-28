def canWinNim(n: int) -> bool:
    return n % 4 != 0


for i in range(1, 100):
    print(i % 4)
    print(canWinNim(i))
