import sys
from itertools import takewhile

DIRS = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}

m = [[x for x in line.rstrip()] for line in takewhile(lambda l: l != "\n", sys.stdin)]

move_marks = [x for line in sys.stdin for x in line.rstrip()]

hlen = len(m)
wlen = len(m[0])

pos = next((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] == "@")


def at(pos: tuple[int, int]) -> str:
    return m[pos[0]][pos[1]]


def put(pos: tuple[int, int], val: str) -> None:
    m[pos[0]][pos[1]] = val


def move(pos: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]:
    return (pos[0] + dir[0], pos[1] + dir[1])


def find_space(pos: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int] | None:
    while True:
        pos = move(pos, dir)
        val = at(pos)
        if val == "#":
            break
        if val == "O":
            continue
        return pos
    return None


def move_boxes(pos: tuple[int, int], dir: tuple[int, int]) -> bool:
    if new_pos := find_space(pos, dir):
        put(new_pos, "O")
        put(pos, ".")
        return True
    return False


for move_mark in move_marks:
    dir = DIRS[move_mark]
    new_pos = move(pos, dir)
    new_val = at(new_pos)
    if new_val == "#" or new_val == "O" and not move_boxes(new_pos, dir):
        continue
    pos = new_pos

total = sum(100 * i + j for i in range(hlen) for j in range(wlen) if at((i, j)) == "O")

assert total == 1552879
