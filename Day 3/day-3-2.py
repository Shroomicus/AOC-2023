input = open('input.txt', 'r')
lines = input.readlines()
total = 0

map = []

adjacencies = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

for line in lines:
    map.append([*(line.replace('\n', ''))])

gearAdj = {}

def isAdjacent(row, col):
    total = 0
    adjGears = []
    while (0 <= row < len(map) and 0 <= col < len(map) and '0' <= map[row][col] <= '9'):
        total = total*10 + int(map[row][col])
        for move in adjacencies:
            if(0 <= row + move[0] < len(map) and 0 <= col + move[1] < len(map)):
                if(map[row+move[0]][col+move[1]] != '.' and not ('0' <= map[row+move[0]][col+move[1]] <= '9')):
                    if((row+move[0], col+move[1]) not in adjGears):
                        adjGears.append((row+move[0], col+move[1]))
        col += 1

    print(adjGears)
    print(total)

    for gear in adjGears:
        if(gear not in gearAdj):
            gearAdj[gear] = []
        gearAdj[gear].append(total)
    
    return len(adjGears) != 0


total = 0
for row in range(len(map)):
    for col in range(len(map[0])):
        if('0' <= map[row][col] <= '9' and isAdjacent(row, col)):
            num = 0
            while (0 <= col < len(map) and '0' <= map[row][col] <= '9'):
                num *= 10
                num += int(map[row][col])
                map[row][col] = '.'
                col += 1
            total += num

for item in map:
    print(item)


print(total)

total = 0
for item in gearAdj:
    print(str(item) + ": " + str(gearAdj[item]))
    if(len(gearAdj[item]) == 2):
        total += gearAdj[item][0] * gearAdj[item][1]

print(total)