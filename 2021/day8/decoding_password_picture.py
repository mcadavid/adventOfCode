import sys

pixels = '123456789012'
LAYER_SIZE = 3 * 2
sys.stdin = open("input.txt")
LAYER_SIZE = 25 * 6
pixels = input()



total = len(pixels)

layers = []

for i in range(0, total, LAYER_SIZE):
    layers.append(pixels[i: i + LAYER_SIZE])

min_number_of_zeros = sys.maxsize
max_index = 0
number_of_ones = 0
number_of_twos = 0
for i in range(len(layers)):
    layer = layers[i]
    if min_number_of_zeros > layer.count('0'):
        min_number_of_zeros = layer.count('0')
        max_index = i
        number_of_twos = layer.count('2')
        number_of_ones = layer.count('1')

print(number_of_twos * number_of_ones)