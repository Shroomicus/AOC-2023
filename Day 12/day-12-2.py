input = open('input2.txt', 'r')
lines = input.readlines()

def getNext(unknown, expected, state):
    next = []
    if(unknown[state[0]] != '.'):
        next.append((state[0]+1, state[1]+1, state[2]))
    if(unknown[state[0]] != '#'):
        if(state[1] > 0):
            next.append((state[0]+1, 0, state[2]+1))
        else:
            next.append((state[0]+1, state[1], state[2]))
    
    return next

def getData(line):
    return [x.count('#') - x.count('?') for x in line.replace('.', ' ').replace('?', " ? ").split()]

def knownData(line):
    return [x.count('#') for x in line.replace('.', ' ').split()]

res = 0
for line in lines[:1]:
    queue = []
    total = 0
    unknown, expected = line.replace('\n', '').split()
    unknown = "?".join(unknown for _ in range(5))
    expected = tuple(int(x) for x in expected.split(','))*5
    print(unknown)
    print(str(expected) + "\n")

    if(unknown[0] != '.'):
        queue.append((1, 1, 0))
    if(unknown[0] != '#'):
        queue.append((1, 0, 0))

    while(len(queue) > 0):
        curr = queue.pop(0)
        print(curr)
        neighbors = getNext(unknown, expected, curr)
        for i in neighbors:
            print(i[0])
            if(i[0] == len(unknown)-1):
                continue
            queue.append(i)
        print()

print("\n" + str(res))

