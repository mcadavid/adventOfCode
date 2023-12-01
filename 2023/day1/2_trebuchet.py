import re

f = open("input.txt", 'r')
sum = 0

digits_map = {
    'one' : '1', 'two': '2', 'three' : '3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'
}

for line in f:   
    line = line.strip()
    
    indizes = []
    for key, value in digits_map.items(): 
        if  key in line:
            indizes += [(m.start(), key) for m in re.finditer(key, line)]
            
    ind = sorted(indizes, key=lambda x:x[0])
   
    if len(ind) > 0:
        key = ind[0][1]
        line = line.replace(key , key + digits_map[key] + key, 1)
        if len(ind) > 1:
            key = ind[-1][1]
            line = line.replace(ind[-1][1], key + digits_map[ind[-1][1]] + key, -1)



    # using regex
    nums = re.findall(r'[0-9]', line)
    
    if len(nums) == 1:
        sum += int(nums[0] + nums[0])
    else:
        sum += int(nums[0] + nums[-1])

print(sum)

