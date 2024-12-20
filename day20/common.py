from collections import OrderedDict

Point = tuple[int, int]

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def setup(m: list[str]):
    hlen = len(m)
    wlen = len(m[0])

    def at(pos: Point) -> str:
        return m[pos[0]][pos[1]]

    def findpath(
        start: Point,
        end: Point,
    ) -> OrderedDict | None:
        visited = OrderedDict()
        steps = 0
        pos = start
        while True:
            visited[pos] = steps
            if pos == end:
                return visited
            for x, y in DIRS:
                if at(new_pos := move(pos, (x, y))) != "#" and new_pos not in visited:
                    steps += 1
                    pos = new_pos
                    break
        return None

    def locate(val: str) -> Point:
        return next((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] == val)

    def move(pos: Point, dir: Point) -> Point:
        return (pos[0] + dir[0], pos[1] + dir[1])

    return findpath, locate, move
