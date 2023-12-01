signals = list(map(eval, open('input').read().split()))
signals = list(map(eval, open('input.txt').read().split()))

def compare(x, y):
    if type(x) == int:
        if type(y) == int:
            return x - y
        else:
            return compare([x], y)
    else:
        if type(y) == int:
            return compare(x, [y])

    for a, b in zip(x, y):
        v = compare(a, b)
        if v:
            return v

    return len(x) - len(y)


def bubble_sort(array):
    n = len(array)
    for i in range(n):
        already_sorted = True
        for j in range(n - i - 1):
            if compare(array[j], array[j + 1]) > 0:
                array[j], array[j + 1] = array[j + 1], array[j] #swap
                already_sorted = False
        if already_sorted:
            break

    return array

signals.append([[2]])
signals.append([[6]])
result = bubble_sort(signals)
#print(result)
i1 = 0
i2 = 0
for i in range(len(signals)):
    if signals[i] == [[2]]:
        i1 = i + 1
        print("2", i)
    elif signals[i] == [[6]]:
        i2 = i + 1
        print("6", i)

print(i1*i2)
