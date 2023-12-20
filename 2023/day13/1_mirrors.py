import re

patterns = open('c:/malu/programming/advent_of_code/adventOfCode/2023/day13/input.txt').read().split('\n\n')


    
result = 0
def check_mirrors_horizontal(pattern):
    n = len(pattern)
    position = 0
   
    mirror = False
    for k in range(1, n):
        if pattern[k] == pattern[k - 1]:
            print("patterns are equal?", pattern[k-1],  pattern[k],  pattern[k-1] == pattern[k])
            mirror = True
            up = k - 2
            down = k + 1
            while up >= 0 and down < n:
                print("patterns are equal?", pattern[up],  pattern[down],  pattern[up] == pattern[down], up, down, k)
                if pattern[up] != pattern[down]:
                    mirror = False
                    break
                up -= 1
                down += 1
        if mirror:
            return k
        
    return position


def rotate_pattern(pattern):
    n = len(pattern)
    m = len(pattern[0])
    rotated = [['']*n for i in range(m)]
    for i in range(m):
        for j in range(n):
            rotated[i][j] = pattern[j][i]

    for i in range(m):
        rotated[i] = ''.join(rotated[i])
    return rotated

    
columns, rows = 0,0
    
def check_mirrors_vertical(pattern):
    rotated = rotate_pattern(pattern)
    return check_mirrors_horizontal(rotated)
    
for p in patterns:  
    p = p.split("\n") 
    print("searching vertical mirror")
    columns += check_mirrors_vertical(p) 
    print("searching horizontal mirror")
    rows += check_mirrors_horizontal(p)

result = columns + 100 * rows
print("Rows:", rows, "Columns", columns)
print(result)
    
