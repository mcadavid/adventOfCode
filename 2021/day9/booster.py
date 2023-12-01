import sys, copy
from itertools import permutations

relative_base = 0


def calc_index(opc, ctr):
    i1 = program[ctr + 1]
    i2 = program[ctr + 2]
    i3 = program[ctr + 3]

    full_code = opc.zfill(5)
    if full_code[0] == '1':
        i3 = ctr + 3
    elif full_code[0] == '2':
        i3 += relative_base

    if full_code[1] == '1':
        i2 = ctr + 2
    elif full_code[1] == '2':
        i2 += relative_base

    if full_code[2] == '1':
        i1 = ctr + 1
    elif full_code[2] == '2':
        i1 += relative_base

    return i1, i2, i3

def calc_index_twos(opc, ctr):
    i1 = program[ctr + 1]
    i2 = program[ctr + 2]

    full_code = opc.zfill(4)
    if full_code[0] == '1':
        i2 = ctr + 2
    elif full_code[0] == '2':
        i2 += relative_base

    if full_code[1] == '1':
        i1 = ctr + 1
    elif full_code[1] == '2':
        i1 += relative_base

    return i1, i2


def calc_index_einfach(opc, ctr):
    i1 = program[ctr + 1]
    if len(opc) == 3 and opc[0] == '1':
        i1 = ctr + 1
    elif len(opc) == 3 and opc[0] == '2':
        i1 += relative_base

    return i1


def read(index):
    if len(program) <= index:
        if index not in extended_memory.keys():
            extended_memory[index] = 0
        return extended_memory[index]
    return program[index]


def write(index, value):
    if len(program) <= index:
        extended_memory[index] = value
    else:
        program[index] = value


def start():
    global relative_base
    opcode = program[0]
    counter = 0
    while opcode != 99:
        s_opcode = str(opcode)
        print(f"idx: {counter} - current opcode: 0{s_opcode[-1]}, {str(opcode).zfill(5)}")
        if s_opcode[-1] == '1':
            index1, index2, index3 = calc_index(s_opcode, counter)
            print(f"Opcode 0{s_opcode[-1]}: Altered {read(index3)} at {index3} to {read(index1) + read(index2)}")
            write(index3, read(index1) + read(index2))
            counter += 4
        elif s_opcode[-1] == '2':
            index1, index2, index3 = calc_index(s_opcode, counter)
            print(f"Opcode 0{s_opcode[-1]}: Altered {read(index3)} at {index3} to {read(index1) * read(index2)}")
            write(index3, read(index1) * read(index2))
            counter += 4
        elif s_opcode[-1] == '3':
            index = calc_index_einfach(s_opcode, counter)
            write(index, input)
            print(f"Opcode 0{s_opcode[-1]}: idx{counter}: Altered {read(index)} at {index} to {input}")
            counter += 2
        elif s_opcode[-1] == '4':
            index = calc_index_einfach(s_opcode, counter)
            counter += 2
            print(f"Opcode 0{s_opcode[-1]}: Output is {read(index)}")
            print(read(index))
        elif s_opcode[-1] == '5':
            index1, index2 = calc_index_twos(s_opcode, counter)
            if read(index1) != 0:
                print(f"Opcode 0{s_opcode[-1]}: {read(index1)} != 0. idx from {counter} to {read(index2)}")
                counter = read(index2)
            else:
                print(f"Opcode 0{s_opcode[-1]}: {read(index1)} == 0. noop")
                counter += 3
        elif s_opcode[-1] == '6':
            index1, index2 = calc_index_twos(s_opcode, counter)
            if read(index1) == 0:
                print(f"Opcode 0{s_opcode[-1]}: idx from {counter} to {read(index2)}")
                counter = read(index2)
            else:
                counter += 3
        elif s_opcode[-1] == '7':
            index1, index2, index3 = calc_index(s_opcode, counter)
            if read(index1) < read(index2):
                print(f"Opcode 0{s_opcode[-1] }: {read(index1)} < {read(index2)}, loc {index3} from {read(index3)} to 1")
                write(index3, 1)
            else:
                print(f"Opcode 0{s_opcode[-1] }: {read(index1)} !< {read(index2)}, loc {index3} from {read(index3)} to 0")
                write(index3, 0)
            counter += 4
        elif s_opcode[-1] == '8':
            index1, index2, index3 = calc_index(s_opcode, counter)
            if read(index1) == read(index2):
                print(f"Opcode 0{s_opcode[-1]}: {read(index1)} == {read(index2)}, loc {index3} from {read(index3)} to 0")
                write(index3, 1)
            else:
                print(f"Opcode 0{s_opcode[-1]}: {read(index1)} != {read(index2)}, loc {index3} from {read(index3)} to 1")
                write(index3, 0)
            counter += 4
        elif s_opcode[-1] == '9':
            index = calc_index_einfach(s_opcode, counter)
            relative_base += read(index)
            counter += 2
            print(f'opcode 9, mode = {s_opcode[0]}, value = {index}')
            print(f"Relative Base now {relative_base}")
        else:
            print("Error")
            break

        opcode = program[counter]






program = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
program = [104,1125899906842624,99]
program = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]

sys.stdin = open("input.txt")
program_input = list(map(int, input().split(',')))
program = copy.copy(program_input)
output = []
input = 2
extended_memory = dict()
start()

