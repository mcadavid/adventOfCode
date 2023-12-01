import re

# Textfile containing the exact input1 given from adventofcode.com
f = open('input2.txt', 'r')
requirements = [r'byr:((19[2-9]\d)|(200[0-2]))',
                r'iyr:(201\d|2020)',
                r'eyr:(202\d|2030)',
                r'hgt:(((1[5-8]\d)|(19[0-3]))cm|((59|6\d|7[0-6])in))',
                r'hcl:#((\d|[a-f]){6})',
                r'ecl:(amb|blu|brn|gry|grn|hzl|oth)',
                r'pid:[0-9]{9}\D']
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
                print(item, "match", line)
                counter += 1

    #print(line)
print(validDocs)
