def islandPerimeter(grid: list[list[int]]) -> int:
    c = 0
    rows = len(grid)
    cols = len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if grid[i][j]:
                c += 4
                if i > 0 and grid[i - 1][j]:
                    c -= 2
                if j > 0 and grid[i][j - 1]:
                    c -= 2
    return c


grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
print(islandPerimeter(grid))
