import sys
from collections import defaultdict
from itertools import chain, combinations

edges = [frozenset(line.rstrip().split("-")) for line in sys.stdin]

graph = defaultdict(set)
for a, b in edges:
    graph[a].add(b)
    graph[b].add(a)

t_nodes = frozenset(x for x in chain.from_iterable(edges) if x.startswith("t"))

clusters = [
    frozenset((t_node, a, b))
    for t_node in t_nodes
    for a, b in combinations(graph[t_node], 2)
    if a in graph[b]
]

total = len(frozenset(clusters))

assert total == 1151
