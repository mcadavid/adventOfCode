grid = open('input.txt', 'r').read().split('\n')

n = len(grid)

def print_grid():
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(grid[i][j], end='')
        print()


for l in range(n):
    grid[l] = list(grid[l])


print_grid()
number_of_0s = []

for column in range(len(grid[0])): 
    for row in range(n):
        moved = False
        if grid[row][column] in '#.':
            continue
        if grid[row][column] == 'O':
            k = row - 1
            while  0 <= k < n - 1 and grid[k][column] == '.':
                k -= 1
                moved = True
            if moved:
                grid[k + 1][column] = 'O'
                grid[row][column] = '.'
i = len(grid)
result = 0
for line in grid:
    result += i * line.count('O')
    i -= 1


print()
print_grid()
print(result)

