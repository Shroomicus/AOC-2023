from collections import defaultdict
from copy import deepcopy
from re import L

input = open('input2.txt', 'r')
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
            map[-1].append('.')
            start = (rowCount, colCount)
            continue
        map[-1].append(char)
    # print(line)

origmap = deepcopy(map)
map[len(map)//2][len(map[1])//2] = 'O'

print(start)

def printMap(pMap):
    for line in pMap:
        res = ""
        for char in line:
            res += char
        print(res)
    print()

def printTotal(pMap):
    total = 0
    for line in pMap:
        for char in line:
            if(char == 'O'):
                total += 1
    return(total)

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

def countSec(total, secData):
    count = 0
    for row in range((len(map) // total) * secData[0], ((len(map) // total)) * (secData[0]+1)):
        for col in range((len(map[0]) // total) * secData[1], ((len(map[0]) // total)) * (secData[1]+1)):
            if(map[row][col] == 'O'):
                count += 1
    return(count)

def printMapData(mapSize):
    res = []
    for i in range(mapSize):
        res.append([])
        for j in range(mapSize):
            res[-1].append(countSec(mapSize, (i, j)))
    for row in res:
        print(row)
    print()

print(len(map)//2)

even = 7693
odd = 7717

print((26501365 - 65) / 131)
print((327 - 65) / 131)

size = 5
map = []
for ind in range(size):
    for row in origmap:
        map.append(row * size)

map[len(map)//2][len(map[1])//2] = 'O'

print(len(map)//2)
for i in range(len(map)//2):
    map = step()
    curr = printTotal(map)

# printMap(map)
printMapData(size)

# for i in range(22):
#     map = step()

# printMapData(size)

print(printTotal(map))
# last = 0
# for i in range(len(map[0])):
#     map = step()
#     curr = printTotal(map)
#     # print(curr)
#     last = curr



# size = 9
# map = []


# printMap(map)

# # res = []
# # for i in range(size):
# #     res.append([])
# #     for j in range(size):
# #         res[-1].append(countSec(size, (i, j)))


# # for row in res:
# #     print(row)