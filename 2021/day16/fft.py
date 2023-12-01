
base_pattern = [0, 1, 0, -1]

counter = 0
output = ''
output = [0, 1, 2, 3, 4, 5, 6, 7, 8]
message = '080871224585914546619083218645595'
message = '019617804207202209144916044189917'
message = '069317163492948606335995924319873'
message = '0' + open("input.txt").read()
output = [int(x) for x in message]





phase = 0
PHASE = 100
while phase < PHASE:
    input = output
    for k in range(1, len(input)):
        i = 0
        counter = 0
        value = 0
        while i < len(input):
            for j in range(k):
                if i == len(input):
                    break
                value += input[i] * base_pattern[counter % 4]
                #print(input[i], "*", base_pattern[counter % 4], end='  +  ')
                #print(i, counter%4)
                i += 1
            counter += 1
        output[k] = abs(value) % 10
        #print("=",abs(value) % 10)
    phase += 1
print(message)
print(*output[1:9])
#94960436