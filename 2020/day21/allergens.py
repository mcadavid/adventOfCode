import itertools


def check_combination(combination):
    for e in directions.keys():
        for i in range(len(combination)):
            food = combination[i]
            allergen = all_list[i]
            if allergen in e and food not in directions[e]:
                return False

    return True


f = open("input1", 'r')
directions = dict()
candidates = dict()
foods = dict()
for line in f:
    line = line[0:-2]
    ingredients, allergens = line.split("(contains ")
    directions[allergens] = ingredients
    ingredients = ingredients.split()
    allergens = allergens.split(', ')
    for a in allergens:
        for i in ingredients:
            if a not in candidates.keys():
                candidates[a] = {i}
            else:
                candidates[a].add(i)

    for i in ingredients:
        if i not in foods.keys():
            foods[i] = 1
        else:
            foods[i] += 1

allergens = candidates.keys()
n = len(allergens)
all_list = list(allergens)

print(candidates)
print(directions)
print(foods)
a = []
counter = 0
for k in all_list:
    a.append(list(candidates[k]))

for combination in itertools.product(*a):
    works = False
    if len(set(combination)) < len(all_list):
        continue
    works = check_combination(combination)
    if works:
        break
    counter += 1

print(combination)
for c in combination:
    foods.pop(c, None)

number_foods = 0
for i in foods.keys():
    number_foods += foods[i]

print(len(foods))
print(counter)
print(len(candidates.keys()))

print("result = ", number_foods)
