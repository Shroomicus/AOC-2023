from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()
input = open('input2.txt', 'r')
lines = input.readlines()

nodes = set()

for line in lines:
    line = line.strip().split(": ")
    nodes.add(line[0])
    for item in line[1].split():
        nodes.add(item)
        G.add_edge(line[0], item, capacity = 1)
        G.add_edge(item, line[0], capacity = 1)
# nx.draw(G, with_labels = True)
# plt.savefig("filename.png")

nodes = list(nodes)
for j in range(1, len(nodes)):
    val, groups = nx.minimum_cut(G, nodes[0], nodes[j])
    if(val == 3):
        print(len(groups[0]) * len(groups[1]))
        break