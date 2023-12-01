import re

f = open("input.txt", 'r')
sum = 0
sum2 = 0
for line in f:    
    # using list comprenhention
    nums = [x for x in line if x.isdigit()] 
    # using regex
    nums_regex = re.findall(r'[0-9]', line)
    
    if len(nums) == 1:
        sum += int(nums[0] + nums[0])
        sum2 += int(nums_regex[0] + nums_regex[0])
    else:
        sum += int(nums[0] + nums[-1])
        sum2 += int(nums_regex[0] + nums_regex[-1])

assert sum == sum2
print(sum, sum2)
