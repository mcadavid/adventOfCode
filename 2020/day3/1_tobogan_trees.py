import sys
sys.stdin = open("input_real.txt")
landscape = ['']*400
RIGHT = 3
DOWN = 1
TREE = '#'
STEP = 1
line = 0
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
trees = 0
col = RIGHT
for r in range(1, rows, STEP):
    if landscape[r][col % cols] == TREE:
        trees += 1
    col += RIGHT

print(trees)
