import sys
input = sys.stdin.readline

grid = [[0] * 9 for i in range(9)]

for i in range(9):
    row = list(map(int, input().split()))
    grid[i] = row

grid_max = -1
max_row, max_col = 0, 0

for i in range(9):
    for j in range(9):
        if grid[i][j] > grid_max:
            grid_max = grid[i][j]
            max_row, max_col = i + 1, j + 1

print(grid_max)
print(max_row, max_col)