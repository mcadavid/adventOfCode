import sys
import heapq

def check_path(pred, new):
    # return True
    p1 = pred
    if p1 not in path:
        return True
    p2 = path[p1]
    if p2 not in path:
        return True
    p3 = path[p2]
    if p3 not in path:
        return True
    p4 =  path[p3]
    if p4 not in path:
        return True
    if len({new, p1, p2, p3, p4}) < 5:
        return True
    if new[0] == p1[0] and p1[0] == p2[0] and p2[0] == p3[0] and p3[0] == p4[0]:
        return False
    if new[1] == p1[1] and p1[1] == p2[1] and p2[1] == p3[1] and p3[1] == p4[1]:
        return False
    return True


def buildPath():
    step = (n-1, n-1)
    print(step, end='->')
    path1 = set()
    acc = int(heat_map[step[0]][step[1]])
    while step !=(0,0):
        path1.add(step)
        step = path[step]
        acc += int(heat_map[step[0]][step[1]])
        print(step, end='->')

    return path1

    

    print("result for path found", acc - int(heat_map[0][0]))


def calculate_distances(starting_vertex):
    distances = {(i,j): sys.maxsize for i in range(n) for j in range(n) }
    distances[starting_vertex] = 0
    
    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        # Nodes can get added to the priority queue multiple times. We only
        # process a vertex the first time we remove it from the priority queue.
        if current_distance > distances[current_vertex]:
            continue

    
        i , j = current_vertex[0], current_vertex[1]
        items = []
        if j > 0:
            items.append((i, j-1)) 
        if j < n - 1:
            items.append((i, j+1))
        if i > 0:
            items.append((i-1, j))
        if i < n - 1:
            items.append((i+1, j))

        for neighbor in items:
            distance = current_distance + int(heat_map[neighbor[0]][neighbor[1]])
            limit = check_path(current_vertex, neighbor)
            #limit = True

            # Only consider this new path if it's better than any path we've
            # already found.
            if limit and distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
                path[neighbor] = current_vertex
       
    return distances

def minimal_heat(start, end, least, most):
    queue = [(0, *start, 0,0)]
    seen = set()
    while queue:
        heat,x,y,px,py = heapq.heappop(queue)
        if (x,y) == end: return heat
        if (x,y, px,py) in seen: continue
        seen.add((x,y, px,py))
        # calculate turns only
        for dx,dy in {(1,0),(0,1),(-1,0),(0,-1)}-{(px,py),(-px,-py)}:
            #print(dx, dy, px, py, end='   ')
            a,b,h = x,y,heat
            # enter 4-10 moves in the chosen direction
            for i in range(1,most+1):
                a,b=a+dx,b+dy
                if (a,b) in board:
                    h += board[a,b]
                    if i>=least:
                        heapq.heappush(queue, (h, a,b, dx,dy))

if __name__ == '__main__':
    # heat_map = open('c:/malu/programming/advent_of_code/adventOfCode/2023/day17/input_init2.txt', 'r').read().split('\n')
    # n = len(heat_map)
    
    # path = {}
    # dists = calculate_distances((0,0))
    # print(dists)
    # print(path)
    # print(dists[(n-1, n-1)])
    # path1 = buildPath()


    

    board = {(i,j): int(c) for i,r in enumerate(open('input.txt')) for j,c in enumerate(r.strip())}
    print(minimal_heat((0,0),max(board), 1, 3))
    print(minimal_heat((0,0),max(board), 4, 10))
