import sys
sys.stdin = open("input_ele.txt")
landscape = ['']*400
TREE = '#'
rows = 0
while True:
    try:
        line = input()
        cols = len(line)
        landscape[rows] = line
        rows += 1
    except EOFError:
        break

print(landscape)
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]
prod = 1
for k in range(5):
    trees = 0
    col = right[k]
    for r in range(down[k], rows, down[k]):
        if landscape[r][col % cols] == TREE:
            trees += 1
        col += right[k]
    prod *= trees
    print(trees)

print(prod)
