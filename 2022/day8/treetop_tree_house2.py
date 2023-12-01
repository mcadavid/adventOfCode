import numpy as np


f = open("input.txt")

forest = []

for line in f:
    forest.append(list(map(int, line[:-1])))

rowsNr =  len(forest)
columnNr = len(forest[0])
print("size", rowsNr, columnNr)
right = [[0 for i in range(rowsNr)]] * columnNr
right = np.array(right)

# from to the right
for i in range(1, rowsNr-1):
    trees = forest[i]
    for j in range(1, columnNr-1):
        right[i,j] = 1
        k = j + 1
        while k < columnNr-1 and trees[k] < trees[j]:
            print(i,j)
            right[i,j] += 1
            k += 1
print("viewing to the right")
print(right)

left = [[0 for i in range(rowsNr)]] * columnNr
left = np.array(left)

# from to the left
for i in range(1, rowsNr-1):
    trees = forest[i]
    for j in range(columnNr-2, 0,-1):
        k = j - 1
        left[i,j] = 1
        while k > 0 and trees[k] < trees[j]:
            left[i,j] += 1
            k = k - 1
print("viewing to the left")
print(left)

down = [[0 for i in range(rowsNr)]] * columnNr
down = np.array(down)
# looking down
for j in range(1, columnNr-1):
    for i in range(1, rowsNr-1):
        k = i+1
        down[i,j] = 1
        while k < rowsNr - 1 and forest[k][j] < forest[i][j]:
            down[i,j] += 1
            k += 1

print("looking down")
print(down)

up = [[0 for i in range(rowsNr)]] * columnNr
up = np.array(up)
# looking up
for j in range(1, columnNr-1):
    for i in range(rowsNr-2, 0,  -1):
        k = i - 1
        up[i,j] = 1
        while k > 0 and forest[k][j] < forest[i][j]:
            up[i,j] += 1
            k -= 1
print("looking up")
print(up)

max_value = 0
for i in range(1,rowsNr-1):
    for j in range(1,columnNr-1):
        value = left[i,j] * right[i,j] * down[i,j] * up[i,j]
        if value > max_value:
            print(i,j)
            max_value = value

print(max_value)




