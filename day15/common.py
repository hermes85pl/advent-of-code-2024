Point = tuple[int, int]

DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def setup(m: list[list[str]]):
    hlen = len(m)
    wlen = len(m[0])

    def at(pos: Point) -> str:
        return m[pos[0]][pos[1]]

    def locate(val: str) -> Point:
        return next((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] == val)

    def locateall(val: str):
        yield from ((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] == val)

    def move(pos: Point, dir: Point) -> Point:
        return (pos[0] + dir[0], pos[1] + dir[1])

    def put(pos: Point, val: str) -> None:
        m[pos[0]][pos[1]] = val

    return at, locate, locateall, move, put
