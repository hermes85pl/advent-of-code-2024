import sys

r1: set[int] = set()
r2: dict[int, int] = {}

for line in sys.stdin:
    a, b = (int(x) for x in line.split())
    r1.add(a)
    r2[b] = r2.get(b, 0) + 1

total = sum(x * r2.get(x, 0) for x in r1)

assert total == 24643097
