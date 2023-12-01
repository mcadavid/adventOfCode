import random
import re
import sys

import intcode


read = open("inputs/25.txt").read().strip()

code = list(map(int, re.findall(r"-?\d+", read)))
prog = intcode.IntCode(code)

sys.stdin = open("input.txt")

original_code = list(map(int, input().split(',')))


def parseOutput(outputStr):
    lines = outputStr.split("\n")
    things = []
    places = []
    i = 0
    while i < len(lines):
        if lines[i].startswith("Items here:"):
            i += 1
            while lines[i].startswith("- "):
                things.append(lines[i][2:])
                i += 1
        elif lines[i].startswith("Doors here lead:"):
            i += 1
            while lines[i].startswith("- "):
                places.append(lines[i][2:])
                i += 1
        else:
            # assert not lines[i].startswith("-")
            i += 1
    return things, places


def tick(inp):
    print("inputting: " + inp)
    inp = [ord(c) for c in inp + "\n"]
    prog.inputs(inp)
    prog.step()
    output = prog.consumeOutputs()
    outputStr = "".join([chr(c) for c in output])
    print("_" * 100)
    print(outputStr)
    print("_" * 100)
    return outputStr


def run(code):
    outputStr = tick("")
    inv = []
    things, places = parseOutput(outputStr)

    # Randomly exploration until collected 8 items and back in pressure sensitive room
    while True:
        if "== Pressure-Sensitive Floor ==" in outputStr and len(inv) == 8:
            # Collected all items and ready to test the weights
            break
        # Go towards a random direction
        outputStr = tick(random.choice(places))
        things, places = parseOutput(outputStr)
        # Take all the things
        for thing in things:
            if thing in [
                "giant electromagnet",
                "infinite loop",
                "photons",
                "escape pod",
                "molten lava",
            ]:
                continue
            outputStr = tick("take " + thing)
            inv.append(thing)

    # Randomly take and drop until you can pass through
    floor = []
    for t in range(10 ** 99):
        outputStr = tick("south")
        if "heavier" in outputStr:
            item = random.choice(floor)
            floor.remove(item)
            inv.append(item)
            outputStr = tick("take " + item)
        elif "lighter" in outputStr:
            item = random.choice(inv)
            inv.remove(item)
            floor.append(item)
            outputStr = tick("drop " + item)
        else:
            print("found after trying", t)
            break

    # Manual mode
    while True:
        print("Waiting for input...")
        inp = input()
        outputStr = tick(inp)


run(code)
