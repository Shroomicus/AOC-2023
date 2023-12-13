input = open('input2.txt', 'r')
lines = input.readlines()

def getNext(unknown, expected, state):
    next = []
    # print(unknown[state[0]])
    if(unknown[state[0]] != '#'):
        if(state[1] == expected[state[2]]):
            if(state[2] < len(expected)-1):
                next.append((state[0]+1, 0, state[2]+1))
            else:
                next.append((state[0]+1, state[1], state[2]))
        if(state[1] == 0):
            next.append((state[0]+1, 0, state[2]))
    if(unknown[state[0]] != '.'):
        if(state[1] < expected[state[2]]):
            next.append((state[0]+1, state[1]+1, state[2]))
    
    removed = 0
    for i in range(len(next)):
        remainder = -1
        for j in range(next[i-removed][2], len(expected)):
            remainder += expected[j] + 1
        remainder -= next[i-removed][1]
        # print(next[i])
        # print(remainder)
        # print(len(unknown) - (next[i-removed][0]-1))
        if(len(unknown) - next[i-removed][0] < remainder):
            del next[i-removed]
            removed += 1
            continue

    return next

def getData(line):
    return [x.count('#') - x.count('?') for x in line.replace('.', ' ').replace('?', " ? ").split()]

def knownData(line):
    return [x.count('#') for x in line.replace('.', ' ').split()]

res = 0
for line in lines:
    queue = []
    total = 0
    unknown, expected = line.replace('\n', '').split()
    unknown = "?".join(unknown for _ in range(5))
    expected = tuple(int(x) for x in expected.split(','))*5
    # expected = tuple(int(x) for x in expected.split(','))
    print(unknown)
    print(str(expected) + "\n")

    if(unknown[0] != '.'):
        queue.append((1, 1, 0))
    if(unknown[0] != '#'):
        queue.append((1, 0, 0))

    while(len(queue) > 0):
        curr = queue.pop(0)
        # print(curr)
        neighbors = getNext(unknown, expected, curr)
        for i in neighbors:
            if(i[0] == len(unknown)):
                if(i[2] == len(expected)-1):
                    if(i[1] == expected[-1]):
                        total += 1
                continue
            queue.append(i)
    print(total)
    res += total

print("\n" + str(res))

