import intcode
import sys, copy

sys.stdin = open("input.txt")
orig_program_input = list(map(int, input().split(',')))


def is_affected(x1, y1):
    computer = intcode.IntCode(copy.copy(orig_program_input))
    computer.inputs = [x1, y1]
    res = computer.run()
    if res == intcode.R_OUTPUT:
        data = computer.read()
        return data == 1
    return False


start_x = 560
start_y = 840
WIDTH = 100
points = set()
x = start_x
y = start_y
stop = False
# for y in range(1250, 1500):
#     for x in range(950,1000):
#         first = is_affected(x, y)
#         if not first:
#             continue
#         else:
#             points.add(tuple([x,y]))
#         second = is_affected(x + 100, y)
#         if first and not second:
#             break
#         if first and second and is_affected(x, 100 + y) and is_affected(x + 100, y):
#             print(x,y)
#             stop = True
#             break
#     if stop:
#         break
#     print()
# 955 1297
# for y in range(1295, 1397):
#     print(y, end="")
#     for x in range(930,1055):
#         if is_affected(x, y):
#             print("#", end="")
#         else:
#             print(".", end="")
#     print()
#

#print(sum(is_affected(x, y) for x in range(50) for y in range(50)))

x = y = 0
while not is_affected(x+99, y):
    y += 1
    while not is_affected(x, y+99):
        x += 1
print(x*10000 + y)
