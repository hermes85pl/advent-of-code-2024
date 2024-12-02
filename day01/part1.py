from heapq import heappop, heappush

h1: list[int] = []
h2: list[int] = []

with open("input.txt") as f:
    while l := f.readline().strip():
        a, b = [int(x) for x in l.split()]
        heappush(h1, a)
        heappush(h2, b)

total = 0
while h1 and h2:
    total += abs(heappop(h1) - heappop(h2))

assert total == 2769675
