import os
import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parent.parent / 'lib'))

import intcode as intcode

MAX_REGISTER_LENGTH = 20


class Scaffold:
    dirs = {"^": -1j, "v": 1j, "<": -1, ">": 1}

    @classmethod
    def init_from_str(cls, s):
        self = Scaffold()

        rows = s.strip().split("\n")
        for y, row in enumerate(rows):
            for x, char in enumerate(row):
                p = x + y * 1j
                if char != ".":
                    self.grid[p] = "#"
                if char in {"^", "v", "<", ">"}:
                    self.bot = [p, self.dirs[char]]

        self.min_x = int(min([p.real for p in self.grid.keys()]))
        self.max_x = int(max([p.real for p in self.grid.keys()]))
        self.min_y = int(min([p.imag for p in self.grid.keys()]))
        self.max_y = int(max([p.imag for p in self.grid.keys()]))

        return self

    def __init__(self):
        self.grid = {}
        self.bot = None

    def __str__(self):
        dir_chars = {v: k for k, v in self.dirs.items()}
        return "\n".join(
            "".join(self.grid.get(x + y * 1j, " ")
                    if self.bot[0] != x + y * 1j else dir_chars[self.bot[1]]
                    for x in range(self.min_x, self.max_x + 1))
            for y in range(self.min_y, self.max_y + 1))

    def intersections(self):
        intersections = []

        for p in self.grid:
            adj = sum(1 for d in self.dirs.values() if p + d in self.grid)
            if adj == 4:
                intersections.append(p)

        return intersections

    def alignment_parameter(self, p):
        return int(p.real * p.imag)

    def path(self):
        path = []
        steps = 0

        while True:
            if self.bot[0] + self.bot[1] in self.grid:
                steps += 1
                self.bot[0] += self.bot[1]
            else:
                if len(path):
                    path.append(str(steps))

                if self.bot[0] + self.bot[1] * -1j in self.grid:
                    self.bot[1] *= -1j
                    path.append("L")
                    steps = 0
                elif self.bot[0] + self.bot[1] * 1j in self.grid:
                    self.bot[1] *= 1j
                    path.append("R")
                    steps = 0
                else:
                    break

        return path


def get_scaffold(codes):
    data = ""
    computer = intcode.IntCode(codes)

    while True:
        res = computer.run()
        if res == intcode.R_HALT:
            break

        elif res == intcode.R_OUTPUT:
            data += chr(computer.read())

    return Scaffold.init_from_str(data)


def drive_bot(codes, main, registers):
    computer = intcode.IntCode(codes)
    computer.edit(0, 2)

    inputs = \
        [ord(x) for x in main] + [ord("\n")] + \
        [ord(x) for x in registers[0]] + [ord("\n")] + \
        [ord(x) for x in registers[1]] + [ord("\n")] + \
        [ord(x) for x in registers[2]] + [ord("\n")] + \
        [ord("n")] + [ord("\n")]

    while True:
        res = computer.run()
        if res == intcode.R_HALT:
            break

        elif res == intcode.R_INPUT:
            computer.write(inputs.pop(0))

        elif res == intcode.R_OUTPUT:
            data = computer.read()

    return data


def find_repeat(path, registers=[], sequence=[]):
    cleared = False
    while not cleared:
        cleared = True

        for i, prev in enumerate(registers):
            if len(prev) <= len(path) and path[:len(prev)] == prev:
                path = path[len(prev):]
                sequence.append(i)
                cleared = False
                break

    # last run
    # either we have consumed all of our path
    # or this is a dead-end
    if len(registers) == 3:
        return (True, registers, sequence) if len(path) == 0 else (False, None, None)

    register_len = min(len(path), MAX_REGISTER_LENGTH // 2)

    # our string form of the path must fit within our register constraint
    # we start on a turn, so we do not want to end on a turn
    # repeats could then be (turn, turn, #), which is not an efficient sequence
    while len(",".join(path[:register_len])) > MAX_REGISTER_LENGTH \
            or path[register_len - 1] in {'R', 'L'}:
        register_len -= 1

    while register_len > 0:
        res, matches, seq = find_repeat(path, registers + [path[:register_len]], sequence.copy())
        if res:
            return res, matches, seq
        register_len -= 2

    return False, [], []


def run():
    MAX_REGISTER = 20

    program = open('input.txt').read().strip()
    codes = [int(x) for x in program.split(",")]

    scaffold = get_scaffold(codes)
    print(f"{scaffold}\n")

    intersections = scaffold.intersections()
    alignments = sum(scaffold.alignment_parameter(x) for x in intersections)
    print(f"Sum of alignment parameters {alignments}")

    _, registers, sequence = find_repeat(scaffold.path())
    main = ",".join(chr(x + ord('A')) for x in sequence)
    regcode = [",".join(x) for x in registers]

    dust = drive_bot(codes, main, regcode)
    print(f"Dust collected: {dust}")


if __name__ == '__main__':
    run()
    sys.exit(0)
