from collections import defaultdict

input = open('input.txt', 'r')
lines = input.readlines()

modules = {}

modules["button"] = ['s', ["broadcaster"]]

for line in lines:
    line = line.strip()
    line = line.split(" -> ")
    if(line[0] == "broadcaster"):
        modules[line[0]] = ['b', line[1].split(', ')]
    if(line[0][0] == '%'):
        # False means off, flip flop
        modules[line[0][1:]] = [line[0][0], line[1].split(', '), False]
    if(line[0][0] == '&'):
        modules[line[0][1:]] = [line[0][0], line[1].split(', '), defaultdict(bool)]

for key in modules:
    for module in modules[key][1]:
        if(module not in modules):
            continue
        # print(module)
        if(modules[module][0] == '&'):
            modules[module][2][key] = False

def pressButton():
    pulses = [0, 0]
    queue = [("broadcaster", False, "button")]
    # False is low, True is high
    # print()
    while(len(queue) > 0):
        # print('\t' + str(queue))
        curr = queue.pop(0)
        # print(curr)
        
        if(curr[1] == False):
            pulses[0] += 1
        else:
            pulses[1] += 1
        if(curr[0] not in modules):
            # print()
            continue
        
        # print(modules[curr[0]])
        # print()
        
        if(curr[0] == "broadcaster"):
            for item in modules[curr[0]][1]:
                queue.append((item, False, curr[0]))
            continue
        
        moduleType = modules[curr[0]][0]


        if(moduleType == '%'):
            if(curr[1] == True):
                continue
            flip = modules[curr[0]][2]
            modules[curr[0]][2] = not flip
            for item in modules[curr[0]][1]:
                queue.append((item, modules[curr[0]][2], curr[0]))
            continue

        if(moduleType == '&'):
            modules[curr[0]][2][curr[2]] = curr[1]
            passed = True
            for key in modules[curr[0]][2]:
                if(modules[curr[0]][2][key] == False):
                    passed = False
                    break
            if(passed):
                for item in modules[curr[0]][1]:
                    queue.append((item, False, curr[0]))
                    # print("HELP")
            else:
                for item in modules[curr[0]][1]:
                    queue.append((item, True, curr[0]))
            continue
        # print(moduleType)
    return pulses

for key in modules:
    print(f"{key} : {modules[key]}")
print()

totalPulses = [0, 0]
for i in range(1000):
    pulseVals = pressButton()
    totalPulses[0] += pulseVals[0]
    totalPulses[1] += pulseVals[1]
    
print()
for key in modules:
    print(f"{key} : {modules[key]}")

print()
print(totalPulses)
print(totalPulses[0] * totalPulses[1])