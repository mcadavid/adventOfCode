import sys

sys.stdin = open("input.txt")
total = 0
all_numbers = []
all_numbers2 = []
RESULT_SUM = 2020
while True:
    try:
        all_numbers.append(int(input()))
    except EOFError:
        break
# all_numbers = [4, 7, 2, 6, 3]
#all_numbers = [1721,979,366,299,675,1456]
print(all_numbers)
an_set = set(all_numbers)
n = len(all_numbers)
for i in range(n):
    for j in range(i, n):
        if RESULT_SUM - all_numbers[i] - all_numbers[j] in an_set:
            print(all_numbers[i], all_numbers[j], RESULT_SUM - all_numbers[i] - all_numbers[j],
                  all_numbers[i] * all_numbers[j] * (RESULT_SUM - all_numbers[i] - all_numbers[j]))
