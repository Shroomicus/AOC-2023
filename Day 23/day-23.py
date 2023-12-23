from collections import defaultdict
from os import path

input = open('input2.txt', 'r')
lines = input.readlines()

map = []
for line in lines:
    line = line.strip()
    map.append(list(line))

dists = defaultdict(int)
paths = {}
dists[(0, 1)] = 0
paths[(0, 1)] = None

queue = [((0, 1), 0, set())]

moves = [((0, 1), '<'), ((0, -1), '>'), ((1, 0), "^"), ((-1, 0), "v")]
while(len(queue) > 0):
    curr = queue.pop(0)
    curr[2].add(curr[0])
    for move in moves:
        dir = move[0]
        newPos = (curr[0][0] + dir[0], curr[0][1] + dir[1])
        if(not( 0 <= newPos[0] < len(map) and  0 <= newPos[1] < len(map[0]))):
            continue
        if(map[newPos[0]][newPos[1]] == '#'):
            continue
        if(map[newPos[0]][newPos[1]] == move[1]):
            continue
        if(newPos in curr[2]):
            continue
        dists[newPos] = curr[1]+1
        paths[newPos] = curr[0]
        
        queue.append((newPos, curr[1] + 1, curr[2].copy()))
    # if(curr[0][0] == len(map)-1):
    #     print("FOUND")
    #     print(curr)
    # print(curr)
pathTiles = []
curr = (len(map)-1, len(map[0])-2)
while(curr != None):
    pathTiles.append(curr)
    curr = paths[curr]
    
for row in range(len(map)):
    res = ""
    for col in range(len(map[0])):
        if((row, col) in pathTiles):
            res += "O"
        else:
            res += map[row][col]
    print(res)

print(dists[(len(map)-1, len(map[0])-2)])
print(paths[(len(map)-1, len(map[0])-2)])