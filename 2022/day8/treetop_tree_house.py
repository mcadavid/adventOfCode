import numpy as np


f = open("input.txt")

forest = []

for line in f:
    forest.append(list(map(int, line[:-1])))

rowsNr =  len(forest)
columnNr = len(forest[0])
print("size", rowsNr, columnNr)
visible = [[False  for i in range(rowsNr)]] * columnNr
visible = np.array(visible)
visible[0] = True
visible[rowsNr-1] = True
for i in range(rowsNr):
    visible[i, 0] = True
    visible[i, columnNr - 1] = True

# from the left
for i in range(1, rowsNr-1):
    trees = forest[i]
    tallest = trees[0]
    for j in range(1, columnNr-1):
        if trees[j] > tallest:
            (visible[i])[j] = True
            tallest = trees[j]


# from the  right
for i in range(1, rowsNr-1):
    trees = forest[i]
    tallest = trees[columnNr - 1]
    for j in range(columnNr-2, 0,-1):
        if trees[j] > tallest:
            (visible[i])[j] = True
            tallest = trees[j]

# from up
for j in range(1, columnNr-1):
    tallest = forest[0][j]
    for i in range(1, rowsNr-1):
        if forest[i][j] > tallest:
            (visible[i])[j] = True
            tallest = forest[i][j]

# from down
for j in range(1, columnNr-1):
    tallest = forest[rowsNr-1][j]
    for i in range(rowsNr-2, 0,  -1):
        if forest[i][j] > tallest:
            (visible[i])[j] = True
            tallest = forest[i][j]

print(visible)

count = 0
for i in range(rowsNr):
    for j in range(columnNr):
        if visible[i, j]:
            count += 1

print(count)




