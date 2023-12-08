input = open('input2.txt', 'r')
lines = input.readlines()
inst = lines[0].replace('\n', '')

moves = {}

for line in lines[2:]:
    moves[line[0:3]] = (line[7:10], line[12:15])

curr = "AAA"
moveNum = 0
while(curr != "ZZZ"):
    val = None
    if(inst[moveNum % len(inst)] == "L"):
        val = 0
    else:
        val = 1
    curr = moves[curr][val]
    moveNum += 1

print(moveNum)