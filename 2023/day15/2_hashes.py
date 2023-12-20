from functools import cache
# @cache

def calculate_hash(step):
    current_value = 0
    for c in step:
        current_value += ord(c)
        current_value *= 17
        current_value = current_value % 256
    return current_value

def calculate_box_number(step):
    a = -1
    label = get_label(step)
    if label in hashes.keys():
        return hashes[label]
    hs = calculate_hash(label)
    hashes[label] = hs 
    return hs

@cache
def get_label(step):
    if '-' in step:
        a = step.index('-')
    elif '=' in step:
        a = step.index('=')
    return step[:a] 


def calculate_focusing_power():
    result = 0
    for i in range(256):
        _, ls = slots[i]
        if len(ls) == 0:
            continue
        for j in range(len(ls)):
            result += (i+1)*(j+1)*int(ls[j])
    return result




if __name__ == "__main__":
    f = open('input.txt', 'r').read().split(',')
    hashes = dict()
    slots = [([],[]) for i in range(256)]

    for step in f:
        box = calculate_box_number(step)
        labels, lengths = slots[box]
        label = get_label(step)
        if label in labels:
            i = labels.index(label)
            if step.endswith('-'):
                labels.remove(label)
                lengths.pop(i)
            else: 
                j = step.index('=')
                lengths[i] = step[j+1]
        else:
            if step.endswith('-'):
                continue
            j = step.index('=')
            labels.append(label)
            lengths.append(step[j+1])
            
                

    # print(hashes)
    print(calculate_focusing_power())