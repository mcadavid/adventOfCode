import sys

sys.stdin = open("input.txt")
total = 0
all_numbers = []
all_numbers2 = []
RESULT_SUM = 2020
while True:
    try:
        all_numbers.append(RESULT_SUM - int(input()))
    except EOFError:
        break
#all_numbers = [4, 7, 2, 6, 3]
#all_numbers = [1721,979,366,299,675,1456]
print(all_numbers)

an_set = set(all_numbers)
for i in all_numbers:
    if RESULT_SUM - i in an_set:
        print(i, RESULT_SUM - i, i * (RESULT_SUM - i))
        break

print(sorted(all_numbers))
sorted(all_numbers, reverse=True)
