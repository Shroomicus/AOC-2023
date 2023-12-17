from collections import defaultdict
import re

input = open('input2.txt', 'r')
lines = input.readlines()

map = []
for line in lines:
    line = line.strip()
    map.append([int(x) for x in list(line)])

# Horizontal moving map, vertical moving map
neighborMap = [[], []]
for row in range(len(map)):
    neighborMap[0].append([])
    neighborMap[1].append([])
    for col in range(len(map[0])):
        neighborMap[0][row].append({})
        neighborMap[1][row].append({})
        dirs =  [(0, 1, 0), (0, -1, 0), (1, 0, 1), (1, 0, -1)]
        for dir in dirs:
            prev = 0
            for num in range(1, 4):
                pos = (dir[0], row + dir[1]*num, col + dir[2]*num)
                if(not (0 <= pos[1] < len(map) and 0 <= pos[2] < len(map[1]))):
                    continue
                prev += map[pos[1]][pos[2]]
            for num in range(4, 11):
                pos = (dir[0], row + dir[1]*num, col + dir[2]*num)
                if(not (0 <= pos[1] < len(map) and 0 <= pos[2] < len(map[1]))):
                    continue
                prev += map[pos[1]][pos[2]]
                neighborMap[(dir[0] + 1) % 2][row][col][pos] = prev

path = {
    (0, 0, 0) : (None, 0),
    (1, 0, 0) : (None, 0)
}
visited = set()

def getMin():
    min = None
    for key in path:
        if(key in visited):
            continue
        if(min == None):
            min = key
        if(path[key][1] < path[min][1]):
            min = key
    return min

max = (0, 0, 0)
while(getMin()):
    currPos = getMin()
    # print(f"{currPos}: {path[currPos]}")
    if(currPos[1] > max[1] and currPos[2] > max[2]):
        max = currPos
        print(max)
    if(currPos[1] == len(map)-1 and currPos[2] == len(map[0])-1):
        print(currPos)
        print(path[currPos])
        break
    # if((1, 1, 5) in visited):
    #     print(currPos)
    #     break
    visited.add(currPos)
    if((currPos[1] * 9 + currPos[2] * 9) < path[currPos][1]):
        continue
    # print()
    # print(currPos)
    # print()
    neighbors = neighborMap[currPos[0]][currPos[1]][currPos[2]]
    # print(neighbors)
    for neighbor in neighbors:
        if(neighbor in visited):
            continue
        if(neighbor in path):
            if(path[neighbor][1] > (path[currPos][1] + neighbors[neighbor])):
                path[neighbor] = (currPos, path[currPos][1] + neighbors[neighbor])
            continue
        if(currPos == (0, 1, 2)):
            print(neighbor)
        path[neighbor] = (currPos, path[currPos][1] + neighbors[neighbor])

# print()

# curr = (1, 12, 12)
# while(path[curr][0] != None):
#     print(path[curr])
#     curr = path[curr][0]

# print(neighborMap[0][1][2])