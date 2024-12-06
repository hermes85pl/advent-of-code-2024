def setup(m: list[str]):
    hlen = len(m)
    wlen = len(m[0])

    def fits(pos: tuple[int, int]) -> str | None:
        if 0 <= pos[0] < hlen and 0 <= pos[1] < wlen:
            return m[pos[0]][pos[1]]
        return None

    return (
        fits,
        next(((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] == "^")),
        (-1, 0),
    )


def turn(dir: tuple[int, int]) -> tuple[int, int]:
    return {(-1, 0): (0, 1), (0, 1): (1, 0), (1, 0): (0, -1), (0, -1): (-1, 0)}[dir]


def move(pos: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]:
    return (pos[0] + dir[0], pos[1] + dir[1])
