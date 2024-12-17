import re
import sys

Point = tuple[int, int]

XMAX = 101
YMAX = 103

XMID = XMAX // 2
YMID = YMAX // 2

PATTERN = re.compile(r"(-?\d+),(-?\d+)")


def robots():
    return ([(int(x), int(y)) for x, y in PATTERN.findall(line)] for line in sys.stdin)


def place(pos: Point, vel: Point, t: int) -> Point:
    return (
        (pos[0] + vel[0] * t) % XMAX,
        (pos[1] + vel[1] * t) % YMAX,
    )
