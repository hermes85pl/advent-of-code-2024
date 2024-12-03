import sys
from heapq import heappop, heappush

h1: list[int] = []
h2: list[int] = []

for line in sys.stdin:
    a, b = (int(x) for x in line.split())
    heappush(h1, a)
    heappush(h2, b)

total = sum(abs(heappop(h1) - heappop(h2)) for _ in range(min(len(h1), len(h2))))

assert total == 2769675
