from functools import cmp_to_key
cardStrings = open('input.txt').read().split('\n')



def getMapPair(line):
    card, bid = line.split()
    return (card, int(bid))


def compare(card1, card2):
    dup1 = {x for x in card1 if card1.count(x) > 1}
    dup2 = {x for x in card2 if card2.count(x) > 1}
    counts1 = sorted([card1.count(x) for x in dup1])
    counts2 = sorted([card2.count(x) for x in dup2])
    value1 = valuesMap.index(counts1)
    value2 = valuesMap.index(counts2)
    if value1 > value2:
        return 1
    if value1 < value2:
        return -1

    for a, b in zip(card1, card2):
        inda = individualValuesMap.index(a)
        indb = individualValuesMap.index(b)
        if inda > indb:
            return 1
        elif inda < indb:
            return -1
    return 0


cardMap = dict(map(getMapPair, cardStrings))

valuesMap = [[5], [4], [2, 3], [3], [2, 2], [2], []]
valuesMap.reverse()

individualValuesMap = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3',  '2']
individualValuesMap.reverse()

sortedList = sorted(list(cardMap.keys()), key=cmp_to_key(compare))
result = 0
for c in sortedList:
    result += (sortedList.index(c) + 1) * cardMap[c]


#print(cardMap)
print(result)
