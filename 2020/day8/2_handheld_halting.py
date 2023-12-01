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

    def __init__(self, commands):
        self.commands = []
        for c in commands:
            self.commands.append(c.copy())

    def add_command(self, command):
        self.commands.append(command)

    def run(self):
        # print("running")
        n = len(self.commands)
        while True:
            if self.current == n:
                return self.accumulator
            c = self.commands[self.current]
            if c.applied:
                return self.accumulator
            c.apply(self)
            # print(self.current)

    def __repr__(self):
        return "Program' current_command = " + str(self.current) + ", accumulator = " + str(self.accumulator) + ", commands = " + str(self.commands)


class Command:
    def __init__(self, name, value, applied=False):
        self.name = name
        self.value = value
        self.applied = applied

    def copy(self):
        pass

    def apply(self, program):
        pass

    def __repr__(self):
        return self.name + " " + str(self.value) + " " + str(self.applied)


class ACC(Command):
    def apply(self, program):
        program.accumulator += self.value
        program.current += 1
        self.applied = True

    def copy(self):
        return ACC(self.name, self.value)


class JUMP(Command):
    def apply(self, program):
        program.current += self.value
        self.applied = True

    def copy(self):
        return JUMP(self.name, self.value)


class NOP(Command):
    def apply(self, program):
        program.current += 1
        self.applied = True

    def copy(self):
        return NOP(self.name, self.value)


def flip(commands, index):
    if commands[index].name == 'jmp':
        return NOP("nop", commands[index].value)
    if commands[index].name == 'nop':
        return JUMP("jmp", commands[index].value)


f = open("input2.txt", 'r')
p = Program([])
for line in f:
    p.add_command(create_command(line))

coms = p.commands
acc = 0
counter = 0
chc = None
print(coms)
while True:
    while coms[counter].name == "acc":
        counter += 1
    chc = coms[counter]
    coms[counter] = flip(coms, counter)
    #print("next run ..................")
    p1 = Program(coms)
    #print(p1)
    p1.run()
    curr = p1.current
    #print(p1)
    if len(coms) == p1.current:
        print(p1)
        acc = p1.accumulator
        break
    chc.applied = False
    coms[counter] = chc
    counter += 1

print(acc)
