import sys

sys.stdin = open("input.txt")

program = list(map(int, input().split(',')))
input = 1


def calc_index(opc):
    i1 = program[counter + 1]
    i2 = program[counter + 2]
    if (len(opc) == 3 and opc[0] == '1') or (len(opc) == 4 and opc[1] == '1'):
        i1 = counter + 1
    if len(opc) == 4 and opc[0] == '1':
        i2 = counter + 2

    return i1, i2


def calc_index_einfach(opc):
    i1 = program[counter + 1]
    if len(opc) == 3 and opc[0] == '1':
        i1 = counter + 1

    return i1


opcode = program[0]
counter = 0
while opcode != 99:
    if str(opcode)[-1] == '1':
        index1, index2 = calc_index(str(opcode))
        program[program[counter + 3]] = program[index1] + program[index2]
        counter += 4
    elif str(opcode)[-1] == '2':
        index1, index2 = calc_index(str(opcode))
        program[program[counter + 3]] = program[index1] * program[index2]
        counter += 4
    elif str(opcode)[-1] == '3':
        index = calc_index_einfach(str(opcode))
        program[index] = input
        counter += 2
    elif str(opcode)[-1] == '4':
        index = calc_index_einfach(str(opcode))
        print(program[index])
        counter += 2
    else:
        print("Error")
        break

    opcode = program[counter]
