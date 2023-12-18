from collections import defaultdict

input = open('input2.txt', 'r')
lines = input.readlines()

instList = [x.strip() for x in lines]

moves = {
    "0" : (0, 1),
    "2" : (0, -1),
    "3" : (-1, 0),
    "1" : (1, 0)
}
moveChars = {
    "R" : (0, 1),
    "L" : (0, -1),
    "U" : (-1, 0),
    "D" : (1, 0)
}

processedMoves = []
for inst in instList:
    # data = inst.split()[2]
    # print(moves[data[-2]])
    # print(int(data[2:len(data)-2], 16))
    data = inst.split()
    move = moveChars[data[0]]
    mult = int(data[1])
    processedMoves.append((move, mult, data[0]))

minVals = [0, 0]
maxVals = [0, 0]
pos = [0, 0]
for mov in processedMoves:
    # print(move)
    move = mov[0]
    mult = mov[1]
    pos[0] += mult * move[0]
    pos[1] += mult * move[1]
    # print(pos)
    if(pos[0] < minVals[0]):
        minVals[0] = pos[0]
    if(pos[1] < minVals[1]):
        minVals[1] = pos[1]
    if(pos[0] > maxVals[0]):
        maxVals[0] = pos[0]
    if(pos[1] > maxVals[1]):
        maxVals[1] = pos[1]

shiftmap = defaultdict(list)
map = defaultdict(list)
pos = [0, 0]
total = 0
last = [0, 0]
for mov in processedMoves:
    move = mov[0]
    mult = mov[1]
    newPos= [pos[0] + mult * move[0], pos[1] + mult * move[1]]
    potentials = (pos[1], newPos[1])
   
    map[newPos[0]].append(newPos[1])
    shiftmap[newPos[0]].append((potentials))

    pos = newPos
    
total = 0
currInds = map[minVals[0]]
currInds.sort()
for i in range(len(currInds) // 2):
    val = currInds[(i*2)+1] - currInds[i*2] + 1
    total += val

for row in range(minVals[0]+1, maxVals[0]):
    shiftmap[row].sort(key = lambda x : x[1])
    print()
    print(shiftmap[row])

    for ind in map[row]:
        if ind in currInds:
            currInds.remove(ind)
        else:
            currInds.append(ind)
    currInds.sort()

    print(currInds)
    for i in range(len(currInds) // 2):
        val = currInds[(i*2)+1] - currInds[i*2] + 1
        total += val
        print(val)

    for i in shiftmap[row]:
        if(i[1] < i[0]):
            total += i[0]-i[1]

for i in range(len(currInds) // 2):
    val = currInds[(i*2)+1] - currInds[i*2] + 1
    total += val

print(total)