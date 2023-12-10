import copy

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

# Clean up map
for col in range(len(map)):
    rowString = ""
    for row in range(len(map[0])):
        if((col, row) not in visited):
           map[col][row] = '.'
        rowString += str(map[col][row])
    print(rowString)

origMap = copy.deepcopy(map)

# Begin expansion down
for col in range(len(map)):
    newCol = []
    for row in range(len(map[0])):
        if(dirs["south"] in dirMap[map[col * 2][row]]):
            newCol.append('|')
        else:
            newCol.append('.')
    map.insert(col*2+1, newCol)

# Begin expansion down
for row in range(len(map[0])):
    newRow = []
    for col in range(len(map)):
        if(dirs["east"] in dirMap[map[col][row*2]]):
            newRow.append('-')
        else:
            newRow.append('.')
    for i in range(len(newRow)):
        map[i].insert(row*2+1, newRow[i])

outside = set()
inside = set()
for col in range(len(map)):
    for row in range(len(map[0])):
        if((map[col][row] == '.' and (col, row) not in outside) and ((col, row) not in inside)):
            queue = [(col, row)]
            currVisited = set()
            isOutside = False
            while(len(queue) > 0):
                curr = queue.pop(0)
                for dir in dirs:
                    move = dirs[dir]
                    if((curr[0] + move[0] not in range(len(map))) or (curr[1]+move[1] not in range(len(map[0])))):
                        isOutside = True
                        continue
                    if(map[curr[0] + move[0]][curr[1] + move[1]] != '.'):
                        continue
                    if((curr[0] + move[0], curr[1] + move[1]) in currVisited):
                        continue
                    currVisited.add((curr[0] + move[0], curr[1] + move[1]))
                    queue.append((curr[0] + move[0], curr[1] + move[1]))

            print(isOutside)
            if(isOutside):
                for i in currVisited:
                    outside.add(i)
            else:
                for i in currVisited:
                    inside.add(i)
            
for col in range(len(origMap)):
    for row in range(len(origMap[0])):
        if((col*2, row*2) in outside):
            origMap[col][row] = 'X'
        
for col in range(len(map)):
    for row in range(len(map[0])):
        if((col, row) in outside):
            map[col][row] = 'X'

for col in range(len(map)):
    rowString = ""
    for row in range(len(map[0])):
        rowString += str(map[col][row])
    print(rowString)

print()

total = 0
for col in range(len(origMap)):
    rowString = ""
    for row in range(len(origMap[0])):
        if(origMap[col][row] == '.'):
            total+=1
        rowString += str(origMap[col][row])
    print(rowString)
print(total)