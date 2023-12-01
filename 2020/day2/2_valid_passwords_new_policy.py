import sys
sys.stdin = open("input.txt")
total = 0
while True:
    try:
        rang, letter, password = input().split()
        range_l, range_r = map(int, rang.split('-'))
        letter = letter[:-1]
        print(range_l, range_r, letter, password)
        count_l = 0
        if (password[range_l - 1] == letter and password[range_r - 1] != letter)\
                or (password[range_l - 1] != letter and password[range_r - 1] == letter):
            total += 1

    except EOFError:
        break

print(total)
