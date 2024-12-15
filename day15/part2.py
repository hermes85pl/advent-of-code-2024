import sys
from itertools import chain, takewhile

widen = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@.",
}

m = [
    list(chain(*[widen[x] for x in line.rstrip()]))
    for line in takewhile(lambda l: l != "\n", sys.stdin)
]

move_marks = [x for line in sys.stdin for x in line.rstrip()]

hlen = len(m)
wlen = len(m[0])

pos = next((i, j) for i in range(hlen) for j in range(wlen) if m[i][j] == "@")

dirs = {"^": (-1, 0), "v": (1, 0), "<": (0, -1), ">": (0, 1)}


def at(pos: tuple[int, int]) -> str:
    return m[pos[0]][pos[1]]


def put(pos: tuple[int, int], val: str) -> None:
    m[pos[0]][pos[1]] = val


def move(pos: tuple[int, int], dir: tuple[int, int]) -> tuple[int, int]:
    return (pos[0] + dir[0], pos[1] + dir[1])


def vertical(dir: tuple[int, int]) -> bool:
    return dir[0] != 0


def box_parts(pos: tuple[int, int]):
    val = at(pos)
    yield pos
    yield move(pos, (0, 1 if val == "[" else -1))


def find_space(pos: tuple[int, int], dir: tuple[int, int]) -> bool:
    stack = list(box_parts(pos)) if vertical(dir) else [pos]
    while stack:
        pos = stack.pop()
        new_pos = move(pos, dir)
        new_val = at(new_pos)
        if new_val == "#":
            return False
        if new_val in "[]":
            if vertical(dir):
                stack.extend(box_parts(new_pos))
            else:
                stack.append(new_pos)
    return True


def move_boxes_surely(pos: tuple[int, int], dir: tuple[int, int]) -> None:
    for pos in box_parts(pos) if vertical(dir) else [pos]:
        new_pos = move(pos, dir)
        new_val = at(new_pos)
        if new_val in "[]":
            move_boxes_surely(new_pos, dir)
        put(new_pos, at(pos))
        put(pos, ".")


def move_boxes(pos: tuple[int, int], dir: tuple[int, int]) -> bool:
    if find_space(pos, dir):
        move_boxes_surely(pos, dir)
        return True
    return False


for move_mark in move_marks:
    dir = dirs[move_mark]
    new_pos = move(pos, dir)
    new_val = at(new_pos)
    if new_val == "#" or new_val in "[]" and not move_boxes(new_pos, dir):
        continue
    pos = new_pos

total = sum(100 * i + j for i in range(hlen) for j in range(wlen) if at((i, j)) == "[")

assert total == 1561175
