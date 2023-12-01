import sys, copy
import intcode

NO_VALUE_SET = 0
ADDR_SET = 1
X_SET = 2
NO_READ = 0
X_READ = 1
computers = [None] * 50



class Computer:
    def __init__(self, address, codes):
        self.address = address
        self.computer = intcode.IntCode(copy.copy(codes))
        self.addr_temp = 0
        self.x_temp = 0
        self.input_queue = []
        self.output_status = NO_VALUE_SET
        self.input_status = NO_READ
        self.temp_y = 0

    def start_computer(self):
        inputs = [self.address]
        res = self.computer.run()
        if res == intcode.R_INPUT:
            self.computer.write(inputs.pop(0))

    def next_run(self):
        res = self.computer.run()
        if res == intcode.R_HALT:
            return

        elif res == intcode.R_INPUT:
            if len(self.input_queue) == 0 and self.input_status != X_READ:
                self.computer.write(-1)
            else:
                if self.input_status == NO_READ:
                    [x, y] = self.input_queue.pop()
                    self.temp_y = y
                    self.computer.write(x)
                    self.input_status = X_READ
                elif self.input_status == X_READ:
                    self.computer.write(self.temp_y)
                    self.input_status = NO_READ

        elif res == intcode.R_OUTPUT:
            state = self.output_status
            data = self.computer.read()
            if NO_VALUE_SET == state:
                self.addr_temp = data
                self.output_status = ADDR_SET
            elif ADDR_SET == state:
                self.x_temp = data
                self.output_status = X_SET
            elif X_SET == state:
                y = data
                self.output_status = NO_VALUE_SET
                if self.addr_temp < 50:
                    goal_computer = computers[self.addr_temp]
                    goal_computer.input_queue.append([self.x_temp, y])
                return self.addr_temp, self.x_temp, y


sys.stdin = open("input.txt")

original_code = list(map(int, input().split(',')))



for i in range(50):
    computer = Computer(i, original_code)
    computer.start_computer()
    computers[i] = computer

counter = 0
while True:
    computer = computers[counter]
    response = computer.next_run()
    if response:
        addr_value, x_value, y_value = response
        print("Output at address ", addr_value, "is", x_value, y_value)
        if addr_value == 255:
            break
    counter += 1
    counter = counter % 50
