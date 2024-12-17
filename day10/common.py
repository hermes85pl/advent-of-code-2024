Point = tuple[int, int]

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def setup(m: list[list[int]]):
    hlen = len(m)
    wlen = len(m[0])

    def at(pos: Point) -> int:
        return m[pos[0]][pos[1]]

    def fits(pos: Point) -> bool:
        return 0 <= pos[0] < hlen and 0 <= pos[1] < wlen

    def move(pos: Point, dir: Point) -> Point:
        return (pos[0] + dir[0], pos[1] + dir[1])

    def moves(pos: Point):
        for dir in DIRS:
            p = move(pos, dir)
            if fits(p):
                yield p

    def steps(pos: Point):
        val = at(pos)
        yield from (x for x in moves(pos) if at(x) - val == 1)

    def trailheads():
        yield from ((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] == 0)

    return at, steps, trailheads
