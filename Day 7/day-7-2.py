from functools import cmp_to_key

input = open('input2.txt', 'r')
lines = input.readlines()

inp = [[x.split()[0], x.split()[1]] for x in lines]

vals = {'A':14, 'K':13, 'Q':12, 'J':0, 'T':10, '9':9, '8':8, '7':7, '6':6, '5':5,'4':4,'3':3,'2':2}

def compare(hand1, hand2):
    hand1 = hand1[0]
    hand2 = hand2[0]
    if(handStrength(hand1) > handStrength(hand2)):
        return 1
    if(handStrength(hand1) < handStrength(hand2)):
        return -1
    
    for i in range(5):
        if(vals[hand1[i]] > vals[hand2[i]]):
            return 1
        if(vals[hand1[i]] < vals[hand2[i]]):
            return -1

def handStrength(hand):
    # 0 high, 1 pair, 2 pair, 3 of a kind, 4 full house, 5 four of a kind, 6 five of a kind
    handDict = {}
    for i in hand:
        if(i not in handDict):
            handDict[i] = 0
        handDict[i] += 1

    if('J' in handDict and handDict['J'] != 5):
        high = 0
        highKey = None
        for i in handDict:
            if(i == 'J'):
                continue
            if(handDict[i] > high):
                high = handDict[i]
                highKey = i
        handDict[highKey] += handDict['J']
        # print(highKey)
        del handDict['J']
    
    if(len(handDict) == 1):
        return 6
    
    if(len(handDict) == 2):
        for i in handDict:
            if(handDict[i] == 4):
                return 5
        return 4
    
    if(len(handDict) == 3):
        for i in handDict:
            if(handDict[i] == 3):
                return 3
        return 2
    
    if(len(handDict) == 4):
        return 1
    
    return 0

# for i in inp:
#     print(i[0])
#     print(handStrength(i[0]))
    
# print(handStrength('JJ3AA'))
# exit()

inp.sort(key=cmp_to_key(compare))
print(inp)

total = 0

for i in range(len(inp)):
    total += int(inp[i][1])*(i+1)
print(total)



'254879637'
'255287056'
'255632664'