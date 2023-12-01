shape_score = dict()
shape_score['X'] = 1
shape_score['Y'] = 2
shape_score['Z'] = 3


game_table = dict()
game_table[('A X')] = 0 + shape_score['Z']
game_table[('A Y')] = 3 + shape_score['X']
game_table[('A Z')] = 6 + shape_score['Y']
game_table[('B X')] = 0 + shape_score['X']
game_table[('B Y')] = 3 + shape_score['Y']
game_table[('B Z')] = 6 + shape_score['Z']
game_table[('C X')] = 0 + shape_score['Y']
game_table[('C Y')] = 3 + shape_score['Z']
game_table[('C Z')] = 6 + shape_score['X']


def score(game):
    return game_table[game]

f = open("input.txt", 'r')
total = 0;
for line in f:
    total += game_table[line[:-1]]

print(total)

