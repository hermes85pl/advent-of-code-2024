def setup(m: list[list[int]]):
    hlen = len(m)
    wlen = len(m[0])

    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def at(pos: tuple[int, int]):
        return m[pos[0]][pos[1]]

    def fits(pos: tuple[int, int]) -> bool:
        return 0 <= pos[0] < hlen and 0 <= pos[1] < wlen

    def move(pos: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]:
        return (pos[0] + dir[0], pos[1] + dir[1])

    def moves(pos: tuple[int, int]):
        for dir in dirs:
            p = move(pos, dir)
            if fits(p):
                yield p

    def steps(pos: tuple[int, int]):
        at_pos = at(pos)
        yield from (x for x in moves(pos) if at(x) - at_pos == 1)

    def trailheads():
        yield from ((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] == 0)

    return at, steps, trailheads
