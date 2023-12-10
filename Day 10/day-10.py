input = open('input.txt', 'r')
lines = input.readlines()

map = [[char for char in line.replace('\n', '')] for line in lines]


dirs = {
    "south" : (1, 0),
    "north" : (-1, 0),
    "west" : (0, -1),
    "east" : (0, 1)
}

dirMap = {
    '.' : {},
    'F' : {dirs["south"], dirs["east"]},
    '|' : {dirs["north"], dirs["south"]},
    '-' : {dirs["west"], dirs["east"]},
    'L' : {dirs["north"], dirs["east"]},
    '7' : {dirs["south"], dirs["west"]},
    'J' : {dirs["north"], dirs["west"]}
}

SPos = None
# Clean up any things leading to edges
for row in range(len(map)):
    for col in range(len(map[0])):
        if(map[row][col] == "S"):
            SPos = (row, col)
            continue
        currDirs = dirMap[map[row][col]]
        for dir in currDirs:
            # print(f"{[row, col]} , {dir}")
            # print(f"{row + dir[0], col + dir[1]}")
            # print(f"{row + dir[0] in range(0, len(map))}")
            if((row + dir[0] not in range(len(map))) or (col+dir[1] not in range(len(map[0])))):
               map[row][col] = '.'
               break

SDirs = set()
# print(dirs)
for i in dirs:
    if((SPos[0] + dirs[i][0] not in range(len(map))) or (SPos[1]+dirs[i][1] not in range(len(map[0])))):
        continue
    isConnected = False
    for dir in dirMap[map[SPos[0]+dirs[i][0]][SPos[1]+dirs[i][1]]]:
        if(map[SPos[0]+dirs[i][0]+dir[0]][SPos[1]+dirs[i][1]+dir[1]] == 'S'):
            isConnected = True
    if(not isConnected):
        continue
    SDirs.add(dirs[i])

print(SDirs)

for i in dirMap:
    # print(dirMap[i])
    # print(SDirs)
    if(SDirs == dirMap[i]):
        map[SPos[0]][SPos[1]] = i
        print(i)
        break

visited = {SPos}
queue = [SPos]
mapLengths = [[None for col in range(len(map[0]))] for col in range(len(map))]
mapLengths[SPos[0]][SPos[1]] = 0

while(len(queue) > 0):
    curr = queue.pop(0)
    for i in dirMap[map[curr[0]][curr[1]]]:
        if((curr[0] + i[0], curr[1] + i[1]) not in visited):
            queue.append((curr[0] + i[0], curr[1] + i[1]))
            mapLengths[curr[0] + i[0]][curr[1] + i[1]] = mapLengths[curr[0]][curr[1]] + 1
            visited.add((curr[0] + i[0], curr[1] + i[1]))

# for i in mapLengths:
    # print(i)

max = 0
for col in mapLengths:
    for val in col:
        if(val and val > max):
            max = val

print(max)