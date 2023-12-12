input = open('input2.txt', 'r')
lines = [x.replace('\n', '') for x in input.readlines()]

for i in lines:
    print(i)

addRows = []
addCols = []
for row in range(len(lines)):
    if(set(lines[row]) == {'.'}):
        addRows.append(row)

for col in range(len(lines[0])):
    isEmpty = True
    for row in range(len(lines)):
        if(lines[row][col] == '#'):
            isEmpty = False
    if(isEmpty):
        addCols.append(col)
        
# print(addRows)
# print(addCols)

for i in range(len(addRows)):
    lines.insert(addRows[i] + i, '.' * len(lines[0]))

for i in range(len(lines)):
    for j in range(len(addCols)):
        lines[i] = lines[i][:(addCols[j]+j)] + '.' + lines[i][(addCols[j]+j):]

print()

for i in lines:
    print(i)

galaxies = []
for row in range(len(lines)):
    for col in range(len(lines[0])):
        if(lines[row][col] == '#'):
            galaxies.append((row, col))
            # lines[row] = lines[row][:col] + str(len(galaxies)) + lines[row][col+1:]

print(galaxies)

def dist(g1, g2):
    return (abs(g2[0] - g1[0]) + abs(g2[1] - g1[1]))

total = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        total += dist(galaxies[i], galaxies[j])
print(total)
