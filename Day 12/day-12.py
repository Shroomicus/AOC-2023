input = open('input2.txt', 'r')
lines = input.readlines()

def getNext(line):
    next = []
    for ind in range(len(line)):
        if line[ind] == '?':
            next.append(line[:ind] + '#' + line[ind+1:])
            next.append(line[:ind] + '.' + line[ind+1:])
            break
    return next

def getData(line):
    return [x.count('#') for x in line.replace('.', ' ').replace('?', " ? ").split()]

res = 0
for line in lines:
    queue = []
    total = 0
    unknown, expected = line.replace('\n', '').split()
    expected = [int(x) for x in expected.split(',')]
    queue.append(unknown)
    # print(expected)
    while(len(queue) > 0):
        curr = queue.pop(0)
        currData = getData(curr)
        failed = False
        for i in range(len(currData)):
            if(i < len(expected)):
                if(currData[i] == 0):
                    break
                if(currData[i] > expected[i]):
                    failed = True
                    # print()
                    # print(getData(curr))
                    # print(expected)
                    break
        if(failed):
            continue
        for i in getNext(curr):
            queue.append(i)
        # print(getData(curr))
        if(curr.count('?') == 0 and currData == expected):
            total += 1
    print(total)
    res += total
print()

print(res)

