import sys

from common import DIRS, Point, setup

m = [[ord(x) for x in line.rstrip()] for line in sys.stdin]

at, fits, move, plots, price = setup(m)


def corners(pos: Point, val: int):
    dirslen = len(DIRS)
    for i in range(dirslen):
        dira = DIRS[i]
        dirb = DIRS[(i + 1) % dirslen]
        dirc = move(dira, dirb)
        posa = move(pos, dira)
        posb = move(pos, dirb)
        posc = move(pos, dirc)
        vala = abs(at(posa)) if fits(posa) else None
        valb = abs(at(posb)) if fits(posb) else None
        valc = abs(at(posc)) if fits(posc) else None
        if vala != val != valb or vala == val == valb and valc != val:
            yield posc


countwalls = lambda pos, val: sum(1 for _ in corners(pos, val))
total = sum(price(pos, countwalls) for pos in plots())

assert total == 911750
