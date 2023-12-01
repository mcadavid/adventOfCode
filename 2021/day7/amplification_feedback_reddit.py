import itertools

with open('input.txt') as f:
    data = [int(token) for token in f.readlines()[0].strip().split(',')]


# Opcode IDs
ADD = 1
MULTIPLY = 2
INPUT = 3
OUTPUT = 4
JUMP_IF_TRUE = 5
JUMP_IF_FALSE = 6
LESS_THAN = 7
EQUALS = 8
HALT = 99


OP_NAMES = {
    ADD: 'Add',
    MULTIPLY: 'Multiply',
    INPUT: 'Input',
    OUTPUT: 'Output',
    JUMP_IF_TRUE: 'Jump If True',
    JUMP_IF_FALSE: 'Jump If False',
    LESS_THAN: 'Less Than',
    EQUALS: 'Equals',
    HALT: 'Halt',
}


# Opcode param lengths
NUM_PARAMS = {
    ADD: 3,
    MULTIPLY: 3,
    INPUT: 1,
    OUTPUT: 1,
    JUMP_IF_TRUE: 2,
    JUMP_IF_FALSE: 2,
    LESS_THAN: 3,
    EQUALS: 3,
    HALT: 0,
}

# Opcode param modes
POSITION_MODE = 0
IMMEDIATE_MODE = 1

ACTION_NEXT = 0
ACTION_JUMP = 1
ACTION_OUTPUT = 2
ACTION_HALT = 3


class Instruction:
    def __init__(self, opcode, length, params, modes, memory):
        self.opcode = opcode
        self.length = length
        self.params = params
        self.modes = modes
        self.memory = memory

    def get_val(self, param_index):
        if self.modes[param_index] == IMMEDIATE_MODE:
            return self.params[param_index]
        elif self.modes[param_index] == POSITION_MODE:
            return self.memory[self.params[param_index]]

    def put_val(self, param_address_index, value):
        self.memory[self.params[param_address_index]] = value

    def return_control(self, action=ACTION_NEXT, value=None):
        return [action, value]


class Add(Instruction):
    def call(self):
        val0 = self.get_val(0)
        val1 = self.get_val(1)
        self.put_val(2, val0 + val1)
        return self.return_control()

class Multiply(Instruction):
    def call(self):
        val0 = self.get_val(0)
        val1 = self.get_val(1)
        self.put_val(2, val0 * val1)
        return self.return_control()


class Input(Instruction):
    def call(self, input_value = None):
        self.put_val(0, input_value)
        return self.return_control()


class Output(Instruction):
    def call(self):
        val = self.get_val(0)
        return self.return_control(ACTION_OUTPUT, val)


class JumpIfTrue(Instruction):
    def call(self):
        in_val = self.get_val(0)
        out_val = self.get_val(1)
        if in_val:
            return self.return_control(ACTION_JUMP, out_val)
        return self.return_control()


class JumpIfFalse(Instruction):
    def call(self):
        in_val = self.get_val(0)
        out_val = self.get_val(1)
        if not in_val:
            return self.return_control(ACTION_JUMP, out_val)
        return self.return_control()


class LessThan(Instruction):
    def call(self):
        val0 = self.get_val(0)
        val1 = self.get_val(1)
        out_val = 1 if val0 < val1 else 0
        self.put_val(2, out_val)
        return self.return_control()


class Equals(Instruction):
    def call(self):
        val0 = self.get_val(0)
        val1 = self.get_val(1)
        out_val = 1 if val0 == val1 else 0
        self.put_val(2, out_val)
        return self.return_control()


class Halt(Instruction):
    def call(self):
        return self.return_control(ACTION_HALT)


OPS = {
    ADD: Add,
    MULTIPLY: Multiply,
    INPUT: Input,
    OUTPUT: Output,
    JUMP_IF_TRUE: JumpIfTrue,
    JUMP_IF_FALSE: JumpIfFalse,
    LESS_THAN: LessThan,
    EQUALS: Equals,
    HALT: Halt,
}


def create_instruction(memory, memory_pointer):
    encoded_opcode = memory[memory_pointer]
    opcode = int(str(encoded_opcode)[-2:])

    num_params = NUM_PARAMS[opcode]

    reverse_modes = str(encoded_opcode)[:-2][::-1]
    modes = [int(char) for char in reverse_modes] + [0] * (num_params - len(reverse_modes))

    params = memory[memory_pointer + 1: memory_pointer + num_params + 1]

    return OPS[opcode](opcode, num_params + 1, params, modes, memory)


class Program:
    def __init__(self, initial_memory):
        self.memory = initial_memory[:]
        self.memory_pointer = 0

    def run(self, input_values):
        input_counter = 0
        while (1):
            instruction = create_instruction(self.memory, self.memory_pointer)

            if instruction.opcode == INPUT:
                action, value = instruction.call(input_values[input_counter])
                input_counter += 1
            else:
                action, value = instruction.call()

            if action == ACTION_NEXT:
                self.memory_pointer += instruction.length
            elif action == ACTION_JUMP:
                self.memory_pointer = value
            elif action == ACTION_HALT:
                break
            elif action == ACTION_OUTPUT:
                self.memory_pointer += instruction.length
                return value


def loop_amplifiers(phase_sequence, data):
    input_signal = 0
    amplifier_index = 0
    is_first_loop = True
    amplifiers = []
    while 1:
        if is_first_loop:
            program = Program(data)
            amplifiers.append(program)
            program_input = [phase_sequence[amplifier_index], input_signal]
        else:
            program = amplifiers[amplifier_index]
            program_input = [input_signal]

        output_signal = program.run(program_input)
        if output_signal is None:
            return input_signal
        input_signal = output_signal
        amplifier_index = (amplifier_index + 1) % 5
        if amplifier_index == 0:
            is_first_loop = False


max_signal = 0
for phase_sequence in itertools.permutations([5,6,7,8,9]):
    max_signal = max(max_signal, loop_amplifiers(phase_sequence, data))
print(max_signal)