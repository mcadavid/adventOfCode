import sys
import heapq


def check_path(k,l, i, j):
    #return True
    print((i,j), (k,l))
    first = (k,l)
    if first not in path:
        return True
    second = path[first]
    if second not in path:
        return True
    third = path[second]
    if third not in path:
        return True
    fourth =  path[third]
    if first[0] == i and first[0] == second[0] and second[0] == third[0] and third[0] == fourth[0]:
        return False
    if first[1] == j and first[1] == second[1] and second[1] == third[1] and third[1] == fourth[1]:
        return False
    return True

def addToHeap(i, j, w, k, l):
    new_distance = w + int(heat_map[i][j])
    if new_distance > shortest[(i,j)]:
        return
    if check_path(k,l, i,j):
        heapq.heappush(minHeap, [new_distance, (i, j)])
        shortest[(i,j)] = new_distance
        path[(i, j)] = (k,l)

def buildPath():
    step = (n-1, n-1)
    print(step, end='->')
    acc = 0
    while step !=(0,0):
        step = path[step]
        print(step[0], step[1])
        acc += int(heat_map[step[0]][step[1]])
        print(step, heat_map[step[0]][step[1]], acc, end='->')

if __name__ == '__main__':
    heat_map = open('input.txt', 'r').read().split('\n')
    n = len(heat_map)
    shortest = {(i,j): sys.maxsize for i in range(n) for j in range(n) }
    shortest[(0,0)] = 0
    path = {}
    minHeap = [[0, (0, 0)]]
    while minHeap:
        current_distance, current_vertex = heapq.heappop(minHeap)
        
        if current_distance > shortest[current_vertex]:
            continue
       

        i, j = current_vertex[0], current_vertex[1]
        
        if j > 0:
            addToHeap(i, j-1, current_distance, i, j)
        if j < n - 1:
            addToHeap(i, j+1, current_distance, i, j)
        if i > 0:
            addToHeap(i-1, j, current_distance, i, j)
        if i < n - 1:
            addToHeap(i+1, j, current_distance, i, j)


    print(shortest)
    print(minHeap)
    print(path)
    print(buildPath())

    