from common import safe

total = 0

with open("input.txt") as f:
    while l := f.readline().strip():
        levels = [int(x) for x in l.split()]
        total += safe(levels)

assert total == 442
