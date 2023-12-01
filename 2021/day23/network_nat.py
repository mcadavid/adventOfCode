import sys, copy
import intcode

NO_VALUE_SET = 0
ADDR_SET = 1
X_SET = 2
NO_READ = 0
X_READ = 1
DONE = 1
CONTINUE = 2
CONTINOUSLY_FLAG = 10
computers = [None] * 50



class NAT:
    def __init__(self):
        self.input_queues = 0
        self.x = 0
        self.y = 0
        self.ys = set()
        self.value_set = False

    def reactivate_network(self):
        if not self.value_set:
            return CONTINUE
        if self.y in self.ys:
            return DONE
        else:
            computers[0].input_queue.append([self.x, self.y])
            self.ys.add(self.y)
            return CONTINUE

    def set(self, x, y):
        self.x = x
        self.y = y
        self.value_set = True


nat = NAT()

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
        self.cont = 0

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
                self.cont += 1
            else:
                if self.input_status == NO_READ:
                    [x, y] = self.input_queue.pop()
                    self.temp_y = y
                    self.computer.write(x)
                    self.input_status = X_READ
                elif self.input_status == X_READ:
                    self.computer.write(self.temp_y)
                    self.input_status = NO_READ
                    if len(self.input_queue) == 0:
                        nat.input_queues -= 1
                self.cont = 0

        elif res == intcode.R_OUTPUT:
            status = self.output_status
            data = self.computer.read()
            if NO_VALUE_SET == status:
                self.addr_temp = data
                self.output_status = ADDR_SET
            elif ADDR_SET == status:
                self.x_temp = data
                self.output_status = X_SET
            elif X_SET == status:
                y = data
                self.output_status = NO_VALUE_SET
                if self.addr_temp < 50:
                    goal_computer = computers[self.addr_temp]
                    goal_computer.input_queue.append([self.x_temp, y])
                    nat.input_queues += 1
                    self.cont = 0
                return self.addr_temp, self.x_temp, y


def idle():
    for c in computers:
        if len(c.input_queue) != 0 or c.cont < CONTINOUSLY_FLAG:
            return False

    return True

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
            nat.set(x_value, y_value)
    if counter % 10 == 0 and idle():
        state = nat.reactivate_network()
        print("Reactivating network. Setting ", nat.x, nat.y, " to computer 0")
        if state == DONE:
            print("Value of twice y", nat.y)
            break

    counter += 1
    counter = counter % 50
