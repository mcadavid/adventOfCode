import re

# Textfile containing the exact input1 given from adventofcode.com
f = open('input2.txt', 'r')
answers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']
validDocs = 0
counter = 0
group = dict.fromkeys(answers, 0)
group_size = 0
for line in f:
    # Checks if the passport was valid and resets the counter to 0 for the next passport
    if line == '\n':
        for item in answers:
            if group[item] == group_size:
                counter += 1
        print(group_size, counter, group)
        group = dict.fromkeys(answers, 0)
        group_size = 0
    # Looks through every line to check for passport details
    else:
        group_size += 1
        for item in answers:
            if re.search(item, line) != None:
                group[item] += 1


print(counter)
