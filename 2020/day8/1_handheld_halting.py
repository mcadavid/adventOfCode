def create_command(line):
    command, value = line.split()
    value = int(value)
    if command == 'acc':
        return ACC("acc", value)
    if command == 'jmp':
        return JUMP("jmp", value)
    if command == 'nop':
        return NOP("nop", value)


class Program:
    accumulator = 0
    commands = []
    current = 0

    def add_command(self, command):
        self.commands.append(command)

    def run(self):
        while True:
            c = self.commands[self.current]
            if c.applied:
                return self.accumulator
            c.apply(self)


class Command:
    def __init__(self, name, value, applied=False):
        self.name = name
        self.value = value
        self.applied = applied

    def apply(self, program):
        pass


class ACC(Command):
    def apply(self, program):
        program.accumulator += self.value
        program.current += 1
        self.applied = True


class JUMP(Command):
    def apply(self, program):
        program.current += self.value
        self.applied = True


class NOP(Command):
    def apply(self, program):
        program.current += 1
        self.applied = True


f = open("input2.txt", 'r')
p = Program()
for line in f:
    p.add_command(create_command(line))

p.run()
print(p.accumulator)
