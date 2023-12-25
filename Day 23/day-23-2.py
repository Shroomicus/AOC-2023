from collections import defaultdict
from os import path

input = open('input.txt', 'r')
lines = input.readlines()

map = []
adjacencies = []
for line in lines:
    line = line.strip()
    map.append(list(line))
    adjacencies.append([])

inters = [(0, 1), (len(map)-1, len(map[0])-2)]

moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for row in range(len(map)):
    for col in range(len(map[0])):
        count = 0
        if(map[row][col] == '#'):
            adjacencies[row].append(count)
            continue
        for move in moves:
            newPos = (row + move[0], col + move[1])
            if(not( 0 <= newPos[0] < len(map) and  0 <= newPos[1] < len(map[0]))):
                continue
            if(map[newPos[0]][newPos[1]] != '#'):
                count += 1
        adjacencies[row].append(count)
        if(count > 2):
            inters.append((row, col))

for row in range(len(map)):
    res = ""
    for col in range(len(map[0])):
        res += map[row][col]
    print(res)

for row in range(len(map)):
    res = ""
    for col in range(len(map[0])):
        res += str(adjacencies[row][col])
    print(res)

connections = {}

for inter in inters:
    visited = []
    queue = [(inter, 0)]
    visited = set()
    connected = []
    while(len(queue) > 0):
        curr = queue.pop(0)
        # print(curr)
        visited.add(curr[0])
        for move in moves:
            newPos = (curr[0][0] + move[0], curr[0][1] + move[1])
            if(not( 0 <= newPos[0] < len(map) and  0 <= newPos[1] < len(map[0]))):
                continue
            if(map[newPos[0]][newPos[1]] == '#'):
                continue
            if(newPos in visited):
                continue
            if(newPos in inters):
                connected.append((newPos, curr[1] + 1))
                continue
            queue.append((newPos, curr[1] + 1))
    # print(inter)
    # print(connected)
    connections[inter] = connected
    # print()

maxes = defaultdict(int)
longest = 0
count = 0
queue = [(inters[0], 0, set())]
while(len(queue) > 0):
    curr = queue.pop(0)
    curr[2].add(curr[0])
    visits = list(curr[2])
    visits.sort(key=lambda x: x[0] + x[1]*len(map))
    key = (curr[0], tuple(visits))
    if(maxes[key] > curr[1]):
        # print(key)
        # print(maxes[key])
        # print(curr[1])
        # print("WHAT HTE FUCK")
        continue
    maxes[key] = curr[1]
    if(curr[0] == connections[inters[1]][0][0]):
        longest = max(curr[1] + connections[inters[1]][0][1], longest)
        # print("SKIP")
        continue
    # print(curr)
    for item in connections[curr[0]]:
        if(item[0] in curr[2]):
            continue
        # print(item)
        # print((item[0], curr[1] + item[1], curr[2].copy()))
        queue.append((item[0], curr[1] + item[1], curr[2].copy()))
        count += 1
    # if(count > 10):
    #     break
        
# print(inters[1])
# print(connections[inters[1]])
print(longest)