input = open('input.txt', 'r')
lines = input.readlines()

from collections import defaultdict

res = 0
for line in lines:
    states = {}
    unknown, expected = line.replace('\n', '').split()
    unknown = "?".join(unknown for _ in range(5))
    expected = tuple(int(x) for x in expected.split(','))*5
    # expected = tuple(int(x) for x in expected.split(','))
    print(unknown)
    print(str(expected) + "\n")

    # Current in group, group num
    if(unknown[0] != '.'):
        states[(1, 0)] = 1
    if(unknown[0] != '#'):
        states[(0, 0)] = 1
    
    for ind in range(1, len(unknown)):
        newStates = defaultdict(int)
        if(unknown[ind] == '#'):
            for state in states:
                if(state[0] < expected[state[1]]):
                    newStates[(state[0] + 1, state[1])] += states[state]
        if(unknown[ind] == '.'):
            for state in states:
                if(state[0] == 0):
                    newStates[(state[0], state[1])] += states[state]
                if(state[0] == expected[state[1]]):
                    if(state[1]+1 < len(expected)):
                        newStates[(0, state[1]+1)] += states[state]
                    else:
                        newStates[(state[0], state[1])] += states[state]
        if(unknown[ind] == '?'):
            for state in states:
                if(state[0] == 0):
                    newStates[(state[0], state[1])] += states[state]
                if(state[0] == expected[state[1]]):
                    if(state[1]+1 < len(expected)):
                        newStates[(0, state[1]+1)] += states[state]
                    else:
                        newStates[(state[0], state[1])] += states[state]
                if(state[0] < expected[state[1]]):
                    newStates[(state[0] + 1, state[1])] += states[state]

        states = newStates
    
    total = 0
    for i in states:
        if(i[1] == len(expected)-1 and i[0] == expected[-1]):
            total += states[i]
    print(total)
    res += total


print("\n" + str(res))

