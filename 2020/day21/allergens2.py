import itertools
import numpy as np


def check_combination(combination):
    for e in directions.keys():
        for i in range(len(combination)):
            food = combination[i]
            allergen = all_list[i]
            if allergen in e and food not in directions[e]:
                return False

    return True

def solve_svd(A,b):
    # compute svd of A
    U,s,Vh = np.linalg.svd(A)

    # U diag(s) Vh x = b <=> diag(s) Vh x = U.T b = c
    c = np.dot(U.T,b)
    # diag(s) Vh x = c <=> Vh x = diag(1/s) c = w (trivial inversion of a diagonal matrix)
    w = np.dot(np.diag(1/s),c)
    # Vh x = w <=> x = Vh.H w (where .H stands for hermitian = conjugate transpose)
    print(np.size(Vh.conj().T))
    print(np.size(w))
    x = np.dot(Vh.conj().T,w)
    return x

f = open("input", 'r')
directions = dict()
candidates = dict()
foods = dict()
food_index = 0
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
            foods[i] = (food_index, 1)
            food_index += 1
        else:
            foods[i] = (foods[i][0], foods[i][1] + 1)



allergens = candidates.keys()
n = len(allergens)
m = len(foods.keys())
all_list = list(allergens)
a = np.zeros((m, m))
for i in range(n):
    for j in foods.keys():
        index = foods[j][0]
        a[i][index] = 0
        if j in candidates[all_list[i]]:
            a[i][index] = 1



print(a)
U, s, Vh = np.linalg.svd(a)
print("s" , s)
print("U", U)
print("Vh", Vh)
print(solve_svd(a, np.array([1,1,1])))

number_foods = 0
for i in foods.keys():
    number_foods += foods[i]



print("candidates", candidates)
print("directions", directions)
print("foods", foods)
a = []
counter = 0
for k in all_list:
    a.append(list(candidates[k]))



number_foods = 0
for i in foods.keys():
    number_foods += foods[i][1]

print("len(foods)", len(foods))
print("counter", counter)
print("len(candidates.keys())", len(candidates.keys()))

print("result = ", number_foods)
