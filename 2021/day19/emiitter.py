import intcode
import sys, copy

sys.stdin = open("input.txt")
orig_program_input = list(map(int, input().split(',')))
points = set()

affected = 0
MAX_VALUE = 400
for y in range(300, MAX_VALUE):
    for x in range(100, MAX_VALUE-200):
        computer = intcode.IntCode(copy.copy(orig_program_input))
        computer.inputs = [x, y]
        res = computer.run()
        if res == intcode.R_OUTPUT:
            data = computer.read()
            if data == 1:
                affected += 1
                points.add(tuple([x, y]))


for y in range(300,MAX_VALUE):
    for x in range(100,MAX_VALUE-200):
        if tuple([x, y]) in points:
            print("#", end="")
        else:
            print(".", end="")
    print()

print(affected)
print(points)
