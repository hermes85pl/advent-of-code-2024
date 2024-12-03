import sys

from common import safe

total = 0

for line in sys.stdin:
    levels = [int(x) for x in line.split()]
    total += any(safe(levels[:i] + levels[i + 1 :]) for i in range(len(levels)))

assert total == 493
