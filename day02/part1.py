import sys

from common import safe

total = 0

for line in sys.stdin:
    levels = [int(x) for x in line.split()]
    total += safe(levels)

assert total == 442
