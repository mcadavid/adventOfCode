import re

patterns = open('input.txt').read().split('\n\n')

smudge_table = dict()

def is_smudge(str1, str2):
    keys = smudge_table.keys()
    if (str1, str2) in keys:
        return smudge_table[(str1, str2)]
    elif (str2, str1) in keys:
        return smudge_table[(str2, str1)]
    found = False
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            if not found:
                found = True 
            else:
                return False
    return found
  
result = 0
def check_mirrors_horizontal(pattern):
    n = len(pattern)
    position = 0
    smudge = False
    mirror = False
    for k in range(1, n):
        smudge = is_smudge(pattern[k], pattern[k-1])
        if pattern[k] == pattern[k - 1] or smudge:
            print("Patterns are equal or almost:", pattern[k-1],  pattern[k],  pattern[k-1] == pattern[k], "Smudge?", smudge, k)
            mirror = True
            up = k - 2
            down = k + 1
            while up >= 0 and down < n:
                print("Are we in smudge state?", smudge)
                if smudge: # patterns have to be equal 
                    print("Patterns are equal?", pattern[up],  pattern[down],  pattern[up] == pattern[down], up, down, k)
                    if pattern[up] != pattern[down]:
                        mirror = False
                        break
                    up -= 1
                    down += 1
                else:
                    smudge = is_smudge(pattern[up], pattern[down])
                    print("Patterns are equal or almost:", pattern[up],  pattern[down],  pattern[up] == pattern[down], "Smudge?", smudge, up, down, k)
                    if smudge or pattern[up] == pattern[down]:
                        up -= 1
                        down += 1
                    else:
                        mirror = False
                        break
                    
        print(mirror, smudge)
        if mirror and smudge:
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
    col_pos = check_mirrors_vertical(p)
    if col_pos > 0:
        columns += col_pos
        continue
    print("\nSearching horizontal mirror")
    rows += check_mirrors_horizontal(p)

result = columns + 100 * rows
print("Rows:", rows, "Columns", columns)
print(result)
    
