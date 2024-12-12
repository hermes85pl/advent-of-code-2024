import sys

from common import setup

m = [[ord(x) for x in line.rstrip()] for line in sys.stdin]

plots, price, corners, _ = setup(m)

countwalls = lambda pos, val: sum(1 for _ in corners(pos, val))
total = sum(price(pos, countwalls) for pos in plots())

assert total == 911750
