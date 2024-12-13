import re
import sys
from itertools import batched

Point = tuple[int, int]

p = re.compile(r"\d+")


def machines():
    return batched(
        ((int(v[0]), int(v[1])) for line in sys.stdin if (v := p.findall(line))),
        3,
    )


def solve(a: Point, b: Point, p: Point) -> int:
    ax, ay = a
    bx, by = b
    px, py = p
    na = round((py / by - px / bx) / (ay / by - ax / bx))
    nb = round((px - na * ax) / bx)
    x = na * ax + nb * bx
    y = na * ay + nb * by
    return 3 * na + nb if x == px and y == py else 0
