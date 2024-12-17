import sys

from common import DIRS, Point, setup

m = [[ord(x) for x in line.rstrip()] for line in sys.stdin]

at, fits, move, plots, price = setup(m)


def walls(pos: Point, val: int):
    for dir in DIRS:
        p = move(pos, dir)
        if not fits(p) or abs(at(p)) != val:
            yield p


countwalls = lambda pos, val: sum(1 for _ in walls(pos, val))
total = sum(price(pos, countwalls) for pos in plots())

assert total == 1488414
