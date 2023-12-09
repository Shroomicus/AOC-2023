input = open('input.txt', 'r')
lines = input.readlines()

total = 0
for line in lines:
    line = [int(x) for x in line.replace('\n', '').split()]

    history = [line]
    while(len(set(history[-1])) != 1):
        new = []
        for i in range(len(history[len(history)-1])-1):
            new.append(history[-1][i+1] - history[-1][i])
        history.append(new)
    # print(history)
    
    for i in range(len(history)-2, -1, -1):
        history[i].insert(0, history[i][0] - history[i+1][0])

    print(history)
    total += history[0][0]

print(total)


# print(line)
# while (set(line) != {0}):
# line = [(line[i+1] - line[i])for i in range(len(line)-1)]
# print(line)