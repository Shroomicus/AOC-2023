input = open('input.txt', 'r')
lines = input.readlines()

pos = []
vel = []

for line in lines:
    line = line.strip().split(' @ ')
    pos.append([int(x) for x in line[0].split(', ')])
    vel.append([int(x) for x in line[1].split(', ')])

def plane(p1, v1, p2, v2):
    p12 = sub(p1, p2)
    v12 = sub(v1, v2)
    vv = cross(v1, v2)
    return (cross(p12, v12), dot(p12, vv))

def cross(a, b):
    return (a[1]*b[2] - a[2]*b[1], a[2]*b[0] - a[0]*b[2], a[0]*b[1] - a[1]*b[0])

def dot(a, b):
    return a[0]*b[0] + a[1]*b[1] + a[2]*b[2]

def sub(a, b):
    return (a[0]-b[0], a[1]-b[1], a[2]-b[2])

def lin(r, a, s, b, t, c):
    x = r*a[0] + s*b[0] + t*c[0]
    y = r*a[1] + s*b[1] + t*c[1]
    z = r*a[2] + s*b[2] + t*c[2]
    return (x, y, z)

def indep(a, b):
    return any(v != 0 for v in cross(a, b))

p1, v1 = pos[0], vel[0]
for ind1 in range(1, len(pos)):
    if(indep(v1, vel[ind1])):
        p2, v2 = pos[ind1], vel[ind1]
        break

for ind2 in range(ind1+1, len(pos)):
    if(indep(v1, vel[ind2]) and indep(v2, vel[ind2])):
        p3, v3 = pos[ind2], vel[ind2]
        break

# print((p1, v1))
# print((p2, v2))
# print((p3, v3))

p0, v0 = ([24, 13, 10], [-3, 1, 2])

print(p1, v1)
print(p2, v2)
print(p3, v3)
print()
a, A = plane(p1, v1, p2, v2)
b, B = plane(p1, v1, p3, v3)
c, C = plane(p2, v2, p3, v3)

w = lin(A, cross(b, c), B, cross(c, a), C, cross(a, b))
t = dot(a, cross(b, c))
w = [round(x / t) for x in w]
print(w)

w1 = sub(v1, w)
w2 = sub(v2, w)
ww = cross(w1, w2)

E = dot(ww, cross(p2, w2))
F = dot(ww, cross(p1, w1))
G = dot(p1, ww)
S = dot(ww, ww)

rock = lin(E, w1, -F, w2, G, ww)
rock = [round(x / S) for x in rock]
sum = 0
print(rock)
for i in rock:
    sum += i
print(sum)