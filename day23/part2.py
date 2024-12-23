import sys
from collections import defaultdict

edges = [set(line.rstrip().split("-")) for line in sys.stdin]

graph = defaultdict(set)
for a, b in edges:
    graph[a].add(b)
    graph[b].add(a)

clusters = edges

for node, neighbors in graph.items():
    for cluster in clusters:
        if cluster.issubset(neighbors):
            cluster.add(node)

cluster = max(clusters, key=len)
password = ",".join(sorted(cluster))

assert password == "ar,cd,hl,iw,jm,ku,qo,rz,vo,xe,xm,xv,ys"
