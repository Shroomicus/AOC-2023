input = open('input2.txt', 'r')
lines = [x.replace('\n', '') for x in input.readlines()]
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
    res = 0
    for i in range(min(g1[0], g2[0]), max(g1[0], g2[0])):
        if(i in addRows):
            res += 1000000
        else:
            res += 1
    for i in range(min(g1[1], g2[1]), max(g1[1], g2[1])):
        if(i in addCols):
            res += 1000000
        else:
            res += 1
    return res

total = 0
for i in range(len(galaxies)):
    for j in range(i, len(galaxies)):
        total += dist(galaxies[i], galaxies[j])
print(total)


# print(dist(galaxies[7], galaxies[8]))