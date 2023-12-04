input = open('input.txt', 'r')
lines = input.readlines()
total = 0

map = []

adjacencies = [[-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]

adjacentGears = []

def isAdjacent(row, col):
    while (0 <= row < len(map) and 0 <= col < len(map) and '0' <= map[row][col] <= '9'):
        for move in adjacencies:
            if(0 <= row + move[0] < len(map) and 0 <= col + move[1] < len(map)):
                if(map[row+move[0]][col+move[1]] != '.' and not ('0' <= map[row+move[0]][col+move[1]] <= '9')):
                    return True
        col += 1
    return False

for line in lines:
    map.append([*(line.replace('\n', ''))])

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