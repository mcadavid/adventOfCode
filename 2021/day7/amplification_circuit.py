import sys, copy
from itertools import permutations


def calc_index(opc, ctr, program_input):
    i1 = program_input[ctr + 1]
    i2 = program_input[ctr + 2]
    if (len(opc) == 3 and opc[0] == '1') or (len(opc) == 4 and opc[1] == '1'):
        i1 = ctr + 1
    if len(opc) == 4 and opc[0] == '1':
        i2 = ctr + 2

    return i1, i2


def calc_index_einfach(opc, ctr, program_input):
    i1 = program_input[ctr + 1]
    if len(opc) == 3 and opc[0] == '1':
        i1 = ctr + 1

    return i1


def calculate_output_amplifier(input1, input2, program):
    opcode = program[0]
    counter = 0
    is_first_input_processed = False
    while opcode != 99:
        s_opcode = str(opcode)
        if s_opcode[-1] == '1':
            index1, index2 = calc_index(s_opcode, counter, program)
            program[program[counter + 3]] = program[index1] + program[index2]
            counter += 4
        elif s_opcode[-1] == '2':
            index1, index2 = calc_index(s_opcode, counter, program)
            program[program[counter + 3]] = program[index1] * program[index2]
            counter += 4
        elif s_opcode[-1] == '3':
            index = calc_index_einfach(s_opcode, counter, program)
            if not is_first_input_processed:
                program[index] = input1
                is_first_input_processed = True
            else:
                program[index] = input2
            counter += 2
        elif s_opcode[-1] == '4':
            index = calc_index_einfach(s_opcode, counter, program)
            counter += 2
            return program[index]
        elif s_opcode[-1] == '5':
            index1, index2 = calc_index(s_opcode, counter, program)
            if program[index1] != 0:
                counter = program[index2]
            else:
                counter += 3
        elif s_opcode[-1] == '6':
            index1, index2 = calc_index(s_opcode, counter, program)
            if program[index1] == 0:
                counter = program[index2]
            else:
                counter += 3
        elif s_opcode[-1] == '7':
            index1, index2 = calc_index(s_opcode, counter, program)
            if program[index1] < program[index2]:
                program[program[counter + 3]] = 1
            else:
                program[program[counter + 3]] = 0
            counter += 4
        elif s_opcode[-1] == '8':
            index1, index2 = calc_index(s_opcode, counter, program)
            if program[index1] == program[index2]:
                program[program[counter + 3]] = 1
            else:
                program[program[counter + 3]] = 0
            counter += 4
        else:
            print("Error")
            break

        opcode = program[counter]


sys.stdin = open("input.txt")
program_input = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
program_input = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23, -1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
program_input = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33, 1002, 33, 7, 33, 1, 33, 31, 31, 1,
                 32, 31, 31, 4, 31, 99, 0, 0, 0]
program_input = list(map(int, input().split(',')))
result = 0
for combination in list(permutations(range(5))):
    input2 = 0
    for i in range(5):
        start_program = copy.copy(program_input)
        input2 = calculate_output_amplifier(combination[i], input2, start_program)
    result = max(result, input2)

print(result)
