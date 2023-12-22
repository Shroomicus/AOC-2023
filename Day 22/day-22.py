from collections import defaultdict

input = open('input2.txt', 'r')
lines = input.readlines()

# x, y, z
# x and y start at 0
cubes = []
maxes = [0, 0, 0]
for line in lines:
    line = line.strip().split('~')
    start = [int(x) for x in line[0].split(',')]
    end = [int(x) for x in line[1].split(',')]
    diff = -1
    for ind in range(3):
        if(start[ind] != end[ind]):
            diff = ind
        maxes[ind] = max((maxes[ind], start[ind]+1, end[ind]+1))
    cubes.append([start, end, diff, start[2]])
    # print(line)

cubes.sort(key= lambda x: x[3])

def makeMap():
    tempMap = []
    for x in range(maxes[0]):
        tempMap.append([])
        for y in range(maxes[1]):
            tempMap[x].append(['-'])
            for z in range(maxes[2]-1):
                tempMap[x][y].append('.')
                # print((x, y, z))

    for cubeInd in range(len(cubes)):
        curr = cubes[cubeInd]
        if(curr[2] == -1):
            pos = curr[0]
            tempMap[pos[0]][pos[1]][pos[2]] = cubeInd
            continue
        for ind in range(curr[0][curr[2]], curr[1][curr[2]]+1):
            pos = curr[0].copy()
            pos[curr[2]] = ind
            tempMap[pos[0]][pos[1]][pos[2]] = cubeInd
    return tempMap

def printX():
    res = ""
    for x in range(maxes[0]):
        res += str(x)
    print(res)
    for z in range(maxes[2]-1, -1, -1):
        res = ""
        for x in range(maxes[0]):
            front =  '.'
            for y in range(maxes[1]):
                if(map[x][y][z] != '.'):
                    front = str(map[x][y][z])
            res += front
        res += str(z)
        print(res)
    print()

map = makeMap()

peaks = []
for x in range(maxes[0]):
    peaks.append([])
    for y in range(maxes[1]):
        peaks[-1].append([1, '-'])

for cubeInd in range(len(cubes)):
# for cubeInd in range(2):
    maxPeak = 0
    supports = set()
    curr = cubes[cubeInd]
    if(curr[2] == 2 or curr[2] == -1):
        curr[1][2] = curr[1][2] - curr[0][2] + peaks[curr[0][0]][curr[0][1]][0]
        curr[0][2] = peaks[curr[0][0]][curr[0][1]][0]
        if(peaks[curr[0][0]][curr[0][1]][1] != '-'):
            supports.add(peaks[curr[0][0]][curr[0][1]][1])
        peaks[curr[0][0]][curr[0][1]] = (curr[1][2] + 1, cubeInd)


    if(curr[2] == 0):
        # print("CURR IS 0")
        
        for ind in range(curr[0][0], curr[1][0] + 1):
            maxPeak = max(maxPeak, peaks[ind][curr[0][1]][0])
        curr[0][2] = maxPeak
        curr[1][2] = maxPeak
        for ind in range(curr[0][0], curr[1][0] + 1):
            if(peaks[ind][curr[0][1]][0] == maxPeak and peaks[ind][curr[0][1]][1] != '-'):
                supports.add(peaks[ind][curr[0][1]][1])
            peaks[ind][curr[0][1]] = (maxPeak+1, cubeInd)
        
    if(curr[2] == 1):
        # print("CURR I-S 1")
        for ind in range(curr[0][1], curr[1][1] + 1):
            maxPeak = max(maxPeak, peaks[curr[0][0]][ind][0])
        curr[0][2] = maxPeak
        curr[1][2] = maxPeak
        for ind in range(curr[0][1], curr[1][1] + 1):
            if(peaks[curr[0][0]][ind][0] == maxPeak and peaks[curr[0][0]][ind][1] != '-'):
                supports.add(peaks[curr[0][0]][ind][1])
            peaks[curr[0][0]][ind] = (maxPeak+1, cubeInd)
        
    cubes[cubeInd].append(supports)
    print(maxPeak)
    print(curr)

for x in range(maxes[0]):
    row = ""
    for y in range(maxes[1]):
        row += str(peaks[x][y]) + " "
    print(row)
# print(maxes)
printX()

map = makeMap()

printX()
# print(peaks)

for cubeInd in range(len(cubes)):
    cubes[cubeInd].append([])

fail = set()
for cubeInd in range(len(cubes)):
    print(cubes[cubeInd])
    cubes[cubeInd]

    if(len(cubes[cubeInd][4]) == 1):
        fail.add(list(cubes[cubeInd][4])[0])

print(fail)
print(len(cubes) - len(fail))
