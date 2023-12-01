import sys

def get_multiplier(position, offset):
    base_pattern = [0, 1, 0, -1]
    if offset < position:
        return base_pattern[0]
    offset -= position
    return base_pattern[(offset // (position+1) + 1) % len(base_pattern)]

def part1(data):
    for _ in range(100):
        for i in range(len(data)):
            data[i] = abs(sum(data[j] * get_multiplier(i, j) for j in range(len(data)))) % 10
    return ''.join(map(str, data[:8]))

def part2(data):
    #offset = int(''.join(map(str, data[:7])))
    #data = (data*10000)[offset:]
    for _ in range(100):
        suffix_sum = 0
        for i in range(len(data)-1, -1, -1):
            data[i] = suffix_sum = (suffix_sum + data[i]) % 10
    return ''.join(map(str, data[:8]))

data = list(map(int, open("input.txt").read()))

message = '80871224585914546619083218645595'
data = [0, 1, 2, 3, 4, 5, 6, 7, 8]
data = [int(x) for x in message]


#print('Part 1: {0}, Part 2: {1}'.format(part1(data[:]), part2(data[:])))

print(part2(data))