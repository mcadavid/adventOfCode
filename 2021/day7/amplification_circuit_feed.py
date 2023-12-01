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


def calculate_output_amplifier(input_value, program):
    opcode = program[0]
    counter = 0
    input_value_counter = 0
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
            program[index] = input_value[input_value_counter]
            input_value_counter += 1
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
    return 99


sys.stdin = open("input.txt")

program_input = list(map(int, input().split(',')))
program_input = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26, 27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6,
                 99, 0, 0, 5]
result = 0
input2 = 0
stored_last_input = 0
output = 0
for combination in list(permutations(range(5, 10))):
    program = copy.copy(program_input)
    first_run = True
    while input2 != 99:
        if first_run:
            for i in range(5):
                input2 = calculate_output_amplifier([combination[i], input2], program)
                if i == 4:
                    stored_last_input = input2
            first_run = False
        else:
            for i in range(5):
                input2 = calculate_output_amplifier([input2], program)
                if i == 4:
                    stored_last_input = input2
        print(stored_last_input)
    result = max(result, stored_last_input)

print(result)
