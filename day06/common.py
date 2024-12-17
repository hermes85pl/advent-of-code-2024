Point = tuple[int, int]


def setup(m: list[str]):
    hlen = len(m)
    wlen = len(m[0])

    def at(pos: Point) -> str | None:
        if 0 <= pos[0] < hlen and 0 <= pos[1] < wlen:
            return m[pos[0]][pos[1]]
        return None

    return (
        at,
        next(((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] == "^")),
        (-1, 0),
    )


def turn(dir: Point) -> Point:
    return {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}[dir]


def move(pos: Point, dir: Point) -> Point:
    return (pos[0] + dir[0], pos[1] + dir[1])
