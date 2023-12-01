import sys

pixels = '123456789012'
LAYER_SIZE = 3 * 2
LENGTH = 3
sys.stdin = open("input.txt")
LAYER_SIZE = 25 * 6
LENGTH = 25
pixels = input()

total = len(pixels)

layers = []

for i in range(0, total, LAYER_SIZE):
    layers.append(pixels[i: i + LAYER_SIZE])

password = []

for counter in range(LAYER_SIZE):
    a = '2'
    i = 0
    while a == '2' and i < len(layers):
        a = layers[i][counter]
        i += 1
    password.append(a)

for i in range(LAYER_SIZE):
    if i % LENGTH == 0:
        print()
    if password[i] == '0':
        print(' ', end='')
    else:
        print('x', end='')

    # print(password[i], end='')

