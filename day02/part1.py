import sys

from common import safe

total = 0

while l := sys.stdin.readline():
    levels = [int(x) for x in l.split()]
    total += safe(levels)

assert total == 442
