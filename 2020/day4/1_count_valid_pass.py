import re
# Textfile containing the exact input1 given from adventofcode.com
f = open('input1.txt', 'r')
requirements = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
validDocs = 0
counter = 0
for line in f:
    # Checks if the passport was valid and resets the counter to 0 for the next passport
    if line == '\n':
        if counter == 7:
            validDocs += 1
        counter = 0
    # Looks through every line to check for passport details
    else:
        for item in requirements:
            if re.search(item, line) != None:
                counter += 1

    print(line)
print(validDocs)



