f = open("input.txt", 'r')


total = 0
number_of_cards = [1]*188
number_of_cards[0] = 0
for line in f:
    line = line.strip().split()
    winning = set()
    own = set()
    c_winning = True
    
    id = 0
    for token in line:
        if token == 'Card': 
            continue
        if token.endswith(':'):
            id = int(token[:-1])
        elif token  == '|':
            c_winning = False
        elif c_winning:
            winning.add(int(token))
        else:
            own.add(int(token))

    result = winning & own
    for i in range(id + 1, len(result) + id + 1):
        number_of_cards[i] += number_of_cards[id]
    # print(number_of_cards, len(result))

total = sum(number_of_cards)
    
    

print(total)

    

    
    