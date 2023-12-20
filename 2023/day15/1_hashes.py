hashes = dict()

def calculate_hash(step):
    current_value = 0
    prefix_value = 0
    for c in step:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256

    print("Hash:", step , current_value)

    return current_value
    


f = open('input_init.txt', 'r').read().split(',')

result = 0
for step in f:
    result += calculate_hash(step)
print(hashes)
print(result)

print(calculate_hash("ot"))