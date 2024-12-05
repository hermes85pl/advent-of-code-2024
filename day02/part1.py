import sys

from common import safe

total = sum(safe([int(x) for x in line.split()]) for line in sys.stdin)

assert total == 442
