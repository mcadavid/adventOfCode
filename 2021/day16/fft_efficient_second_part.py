import copy
counter = 0
output = ''
output = [0, 1, 2, 3, 4, 5, 6, 7, 8]
message = '019617804207202209144916044189917'
message = '069317163492948606335995924319873'
message = '03036732577212944063491565474664' * 10000
message = '0' + open("input.txt").read() * 100000
offset = int(message[0:7])
print("offset:", offset)
output = [int(x) for x in message]

base_pattern = [0, 1, 0, -1]

phase = 0
PHASE = 100

n = len(output)
while phase < PHASE:
    input = output
    for k in range(1, n):
        value = 0
        for i in range(n // k + 1):
            if i % 4 == 1:
                value += sum(input[i * k: (i + 1) * k])
            elif i % 4 == 3:
                value -= sum(input[i * k: (i + 1) * k])
        output[k] = abs(value) % 10
    phase += 1

print("phase", phase)
print(*output[offset: offset + 9])
# 94960436
