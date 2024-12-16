import sys

Point = tuple[int, int]

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def setup():
    m = [line.rstrip() for line in sys.stdin]

    def at(pos: Point) -> str:
        return m[pos[0]][pos[1]]

    def locate(val: str) -> Point:
        return next(
            (i, j) for i in range(len(m)) for j in range(len(m[0])) if m[i][j] == val
        )

    def move(pos: Point, dir: Point) -> Point:
        return (pos[0] + dir[0], pos[1] + dir[1])

    def turn(dir: Point, clockwise: bool) -> Point:
        return DIRS[(DIRS.index(dir) + (1 if clockwise else -1)) % len(DIRS)]

    return at, locate, move, turn
