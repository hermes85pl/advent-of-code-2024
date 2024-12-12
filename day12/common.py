from typing import Callable


def setup(m: list[list[int]]):
    hlen = len(m)
    wlen = len(m[0])

    dirs = ((0, 1), (1, 0), (0, -1), (-1, 0))

    def at(pos: tuple[int, int]) -> int:
        return m[pos[0]][pos[1]]

    def put(pos: tuple[int, int], val: int) -> None:
        m[pos[0]][pos[1]] = val

    def fits(pos: tuple[int, int]) -> bool:
        return 0 <= pos[0] < hlen and 0 <= pos[1] < wlen

    def move(pos: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]:
        return (pos[0] + dir[0], pos[1] + dir[1])

    def walls(pos: tuple[int, int], val: int):
        for dir in dirs:
            p = move(pos, dir)
            if not fits(p) or abs(at(p)) != val:
                yield p

    def corners(pos: tuple[int, int], val: int):
        dirslen = len(dirs)
        for i in range(dirslen):
            dira = dirs[i]
            dirb = dirs[(i + 1) % dirslen]
            dirc = move(dira, dirb)
            posa = move(pos, dira)
            posb = move(pos, dirb)
            posc = move(pos, dirc)
            vala = abs(at(posa)) if fits(posa) else None
            valb = abs(at(posb)) if fits(posb) else None
            valc = abs(at(posc)) if fits(posc) else None
            if (vala != val and valb != val) or (
                vala == val and valb == val and valc != val
            ):
                yield posc

    def moves(pos: tuple[int, int]):
        for dir in dirs:
            p = move(pos, dir)
            if fits(p):
                yield p

    def steps(pos: tuple[int, int], val: int):
        yield from (x for x in moves(pos) if at(x) == val)

    def price(
        pos: tuple[int, int], countwalls=Callable[[tuple[int, int], int], int]
    ) -> int:
        stack = [pos]
        cell_count = 0
        wall_count = 0
        while stack:
            pos = stack.pop()
            val = at(pos)
            if val > 0:
                stack.extend(steps(pos, val))
                cell_count += 1
                wall_count += countwalls(pos, val)
                put(pos, -val)
        return cell_count * wall_count

    def plots():
        yield from ((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] > 0)

    return plots, price, corners, walls
