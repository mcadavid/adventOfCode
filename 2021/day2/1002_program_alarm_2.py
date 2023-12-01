import sys, itertools, copy

sys.stdin = open("input.txt")

program = [1,9,10,3,2,3,11,0,99,30,40,50]
program = [1,0,0,0,99]
program = [2,3,0,3,99]
program = [2,4,4,5,99,0]
program = [1,1,1,4,99,5,6,0,99]

original = list(map(int, input().split(',')))



for noun, verb in itertools.product(range(100), range(100)):

    program = copy.copy(original)
    program[1] = noun
    program[2] = verb

    opcode = program[0]
    counter = 0
    while opcode != 99:
        if opcode == 1:
            program[program[counter + 3]] = program[program[counter + 1]] + program[program[counter + 2]]
        elif opcode == 2:
            program[program[counter + 3]] = program[program[counter + 1]] * program[program[counter + 2]]
        else:
            "Error"
            break
        counter += 4
        opcode = program[counter]

    if program[0] == 19690720:
        break

print(100 * noun + verb)
print(noun, verb)