f = open("input.txt", 'r')

sum = 0
for line in f:
    line = line.strip().split()
    winning = set()
    own = set()
    c_winning = True
    for token in line:
        if token == 'Card' or token.endswith(':'):
            continue
        if token  == '|':
            c_winning = False
        elif c_winning:
            winning.add(int(token))
        else:
            own.add(int(token))

    result = winning & own
    
    if len(result) > 0:
        #print(result, len(result), 1 << len(result) - 1)
        sum += 1 << len(result) - 1

print(sum)

    

    
    