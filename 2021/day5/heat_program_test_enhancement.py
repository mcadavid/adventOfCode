import sys

sys.stdin = open("input.txt")

relative_base = 0





def calc_index(opc):
    i1 = program[counter + 1]
    i2 = program[counter + 2]
    if (len(opc) == 3 and opc[0] == '1') or (len(opc) == 4 and opc[1] == '1'):
        i1 = counter + 1
    if len(opc) == 4 and opc[0] == '1':
        i2 = counter + 2
    if (len(opc) == 3 and opc[0] == '2') or (len(opc) == 4 and opc[1] == '2'):
        i1 = counter + relative_base
    if len(opc) == 4 and opc[0] == '2':
        i2 = counter + relative_base

    return i1, i2


def calc_index_einfach(opc):
    i1 = program[counter + 1]
    if len(opc) == 3 and opc[0] == '1':
        i1 = counter + 1

    return i1


# program = [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8]
# program = [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8]
# program = [3, 3, 1108, -1, 8, 3, 4, 3, 99]
# program = [3, 3, 1107, -1, 8, 3, 4, 3, 99]
# program = [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9]
# program = [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
# program = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20,
#            4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]


program = list(map(int, input().split(',')))
input = 5


opcode = program[0]
counter = 0;
while opcode != 99:
    s_opcode = str(opcode)
    if s_opcode[-1] == '1':
        index1, index2 = calc_index(s_opcode)
        program[program[counter + 3]] = program[index1] + program[index2]
        counter += 4
    elif s_opcode[-1] == '2':
        index1, index2 = calc_index(s_opcode)
        program[program[counter + 3]] = program[index1] * program[index2]
        counter += 4
    elif s_opcode[-1] == '3':
        index = calc_index_einfach(s_opcode)
        program[index] = input
        counter += 2
    elif s_opcode[-1] == '4':
        index = calc_index_einfach(s_opcode)
        print(program[index])
        counter += 2
    elif s_opcode[-1] == '5':
        index1, index2 = calc_index(s_opcode)
        if program[index1] != 0:
            counter = program[index2]
        else:
            counter += 3
    elif s_opcode[-1] == '6':
        index1, index2 = calc_index(s_opcode)
        if program[index1] == 0:
            counter = program[index2]
        else:
            counter += 3
    elif s_opcode[-1] == '7':
        index1, index2 = calc_index(s_opcode)
        if program[index1] < program[index2]:
            program[program[counter + 3]] = 1
        else:
            program[program[counter + 3]] = 0
        counter += 4
    elif s_opcode[-1] == '8':
        index1, index2 = calc_index(s_opcode)
        if program[index1] == program[index2]:
            program[program[counter + 3]] = 1
        else:
            program[program[counter + 3]] = 0
        counter += 4
    elif s_opcode[-1] == '9':
        index = calc_index_einfach(s_opcode)
        relative_base = program[index] + relative_base
    else:
        print("Error")
        break

    opcode = program[counter]
