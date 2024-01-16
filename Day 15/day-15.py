from collections import defaultdict

input = open('input2.txt', 'r')
seq = input.readlines()[0].strip().split(',')
print(seq)

boxes = []
for i in range(256):
    boxes.append(defaultdict(int))

for item in seq:
    res = 0
    for char in item:
        if(char == '='):
            boxes[res][item.split('=')[0]] = int(item.split('=')[1])
            break
        if(char == '-'):
            if(item.split('-')[0] in boxes[res]):
                del boxes[res][item.split('-')[0]]
            continue
        res += ord(char)
        res = (res * 17) % 256

total = 0
for key in range(len(boxes)):
    print(f"{key} : {boxes[key]}")
    count = 0
    for subkey in boxes[key]:
        count += 1
        print(boxes[key][subkey])
        total += (key + 1) * count * boxes[key][subkey]
print(total)
        
