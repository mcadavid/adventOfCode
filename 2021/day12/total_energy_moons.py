import itertools, sys


def apply_gravity():
    for pair in list(itertools.combinations(range(4), 2)):
        for i in range(3):
            if positions[pair[0]][i] < positions[pair[1]][i]:
                velocities[pair[0]][i] += 1
                velocities[pair[1]][i] -= 1
            elif positions[pair[0]][i] > positions[pair[1]][i]:
                velocities[pair[0]][i] -= 1
                velocities[pair[1]][i] += 1


def apply_velocity():
    for moon in range(4):
        for i in range(3):
            positions[moon][i] += velocities[moon][i]



def calculate_total_energy():
    total_energy = 0
    for moon in range(4):
        kinetic_energy = 0
        potential_energy = 0
        for i in range(3):
            potential_energy += abs(positions[moon][i])
            kinetic_energy += abs(velocities[moon][i])

        total_energy += kinetic_energy * potential_energy
    return total_energy


positions = dict()
velocities = dict()
codes = set();

STEPS = 3000
positions = {0: [-1, 0, 2], 1: [2, -10, -7], 2: [4, -8, 8], 3: [3, 5, -1]}
velocities = {0: [0, 0, 0], 1: [0, 0, 0], 2: [0, 0, 0], 3: [0, 0, 0]}

#positions = {0:[-8, -10, 0], 1:[5, 5, 10], 2:[2, -7, 3], 3:[9, -8, -3]}
#positions = {0:[3, -6, 6], 1:[10, 7, -9], 2:[-3, -7, 9], 3:[-8, 0, 4]}

time = 0

while True:
    apply_gravity()
    apply_velocity()

    code = ' ' + str(positions) + str(velocities)
    if code in codes:
        print(time)
        print(codes)
        break;
    codes.add(code)
    time += 1

print("First part: ", calculate_total_energy())


