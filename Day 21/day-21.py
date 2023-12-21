from collections import defaultdict
from copy import deepcopy

input = open('input.txt', 'r')
lines = input.readlines()

map = []
start = None
rowCount = -1
for line in lines:
    rowCount += 1
    line = line.strip()
    map.append([])
    colCount = -1
    for char in line:
        colCount += 1
        if(char == 'S'):
            map[-1].append('O')
            start = (rowCount, colCount)
            continue
        map[-1].append(char)
    # print(line)

print(start)

def printMap(pMap):
    total = 0
    for line in pMap:
        res = ""
        for char in line:
            if(char == 'O'):
                total += 1
            res += char
        print(res)
    print(total)
    print()

def step():
    dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    newMap = deepcopy(map)
    for row in range(len(newMap)):
        for col in range(len(newMap[0])):
            if(map[row][col] == 'O'):
                newMap[row][col] = '.'
                for dir in dirs:
                    if(not(0 <= row + dir[0] < len(newMap) and 0 <= col + dir[1] < len(newMap[0]))):
                        continue
                    if(map[row + dir[0]][col + dir[1]] == '.'):
                        newMap[row + dir[0]][col + dir[1]] = 'O'
    return newMap

printMap(map)

for i in range(64):
    map = step()

printMap(map)