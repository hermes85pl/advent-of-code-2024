import sys

from common import safe

total = 0

while l := sys.stdin.readline():
    levels = [int(x) for x in l.split()]
    total += any(safe(levels[:i] + levels[i + 1 :]) for i in range(len(levels)))

assert total == 493
