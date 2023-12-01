import random
import copy

rules = {
    0: [[1, 2]],
    1: [["a"]],
    2: [[1, 3], [3, 1]],
    3: [["b"]]
}


def expand(start, expansion):
    pick = ''
    if start in rules.keys():
        pick = random.choice(rules[start])
        # print(pick)
        for r in pick:
            expand(r, expansion)
    else:
        expansion.append(start)
    return expansion


def expand_grammar():
    result = ""
    for i in range(1000):
        start = 0
        expansion = []
        r = expand(start, expansion)
        s.add(result.join(r))


def matches_rule(chars, rule):
    #print(rule)
    if rule in terminal.keys():
        #print(chars)
        if len(chars) == 0:
            return False
        if len(chars) != 0 and chars[0] == terminal[rule]:
            chars.pop(0)
            return True
        return False
    else:
        all_sub_rules = rules[rule]
        for sr in all_sub_rules: # OR
            chars_copy = copy.deepcopy(chars)
            matches = True
            for r in sr:
                if not matches_rule(chars_copy, r): # AND
                    matches = False
                    break

            if matches:
                while len(chars) > len(chars_copy):
                    chars.pop(0)
                return True

    return False


f = open("input3", 'r')
rules = dict()
terminal = dict()
expand_g = False
counter = 0
s = set()
for line in f:
    line = line[0:-1]
    if len(line) == 0 and not expand_g:
        # expand_grammar()
        expand_g = True
    elif not expand_g:
        key, value = line.split(': ')
        key = int(key)
        values = []
        if value == '"a"' or value == '"b"':
            terminal[key] = value[1]
        else:
            for e in value.split('|'):
                if value[0] == '"':
                    values.append(value[1])
                values.append(list(map(int, e.split())))
            rules[key] = values
    elif expand_g:
        chars1 = list(line)
        if matches_rule(chars1, 0) and len(chars1) == 0:
            print(line)
            counter += 1

print(rules)

expansion = []

print(len(s))
print(counter)
