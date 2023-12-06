input = open('input.txt', 'r')
lines = input.readlines()

times = [int(x) for x in (lines[0][5:].split())]
dists = [int(x) for x in (lines[1][10:].split())]

print(times)
print(dists)

def distTime(timeHeld, totalTime):
    return (totalTime - timeHeld) * timeHeld

total = 1
for ind in range(len(times)):
    waysWon = 0
    for i in range(times[ind]):
        if(distTime(i, times[ind]) > dists[ind]):
            waysWon += 1
    total *= waysWon

# print(distTime(1, 7))

print(total)