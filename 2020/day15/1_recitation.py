lines = dict()
lines["0,3,6"] = 436
lines["1,3,2"] = 1
lines["2,1,3"] = 10
lines["1,2,3"] = 27
lines["2,3,1"] = 78
lines["3,2,1"] = 438
lines["3,1,2"] = 1836


def test():
    for l in lines.keys():
        c = list(map(int, l.split((','))))
        val = calculate(c)
        print(val)
        if lines[l] != val:
            print("Error!!!", val, lines[l])
            break


def calculate(nums):
    col = dict()
    for i in range(1, len(nums) + 1):
        col[nums[i-1]] = (i,i)
    counter = len(nums)
    last_spoken = nums[len(nums) - 1]
    while counter < 2020:
        last_spoken = counter - col[last_spoken][1]
        #print(last_spoken)
        if not last_spoken in col.keys():
            col[last_spoken] = (counter + 1, counter + 1)
        col[last_spoken] = (counter + 1, col[last_spoken][0])
        counter += 1

    return last_spoken

print(calculate([0,13,1,16,6,17]))

