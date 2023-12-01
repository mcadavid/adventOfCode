import sys
sys.stdin = open("input.txt")
total = 0
while True:
    try:
        range, letter, password = input().split()
        range_l, range_r = map(int, range.split('-'))
        letter = letter[:-1]
        print(range_l, range_r, letter, password)
        count_l = 0
        for l in password:
            if l == letter:
                count_l += 1
        if range_l <= count_l <= range_r:
            total += 1
    except EOFError:
        break

print(total)
