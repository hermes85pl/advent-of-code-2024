import sys
from itertools import chain, takewhile

from common import DIRS, Point, setup

WIDER_COUNTERPARTS = {
    "#": "##",
    "O": "[]",
    ".": "..",
    "@": "@.",
}

m = [
    list(chain.from_iterable(WIDER_COUNTERPARTS[x] for x in line.rstrip()))
    for line in takewhile(lambda l: l != "\n", sys.stdin)
]

move_marks = [x for line in sys.stdin for x in line.rstrip()]

at, locate, locateall, move, put = setup(m)

pos = locate("@")


def vertical(dir: Point) -> bool:
    return dir[0] != 0


def box_parts(pos: Point):
    return (pos, move(pos, (0, 1 if at(pos) == "[" else -1)))


def find_space(pos: Point, dir: Point) -> bool:
    for pos in box_parts(pos) if vertical(dir) else (pos,):
        new_pos = move(pos, dir)
        new_val = at(new_pos)
        if new_val == "#" or new_val in "[]" and not find_space(new_pos, dir):
            return False
    return True


def move_boxes_surely(pos: Point, dir: Point) -> None:
    for pos in box_parts(pos) if vertical(dir) else (pos,):
        new_pos = move(pos, dir)
        new_val = at(new_pos)
        if new_val in "[]":
            move_boxes_surely(new_pos, dir)
        put(new_pos, at(pos))
        put(pos, ".")


def move_boxes(pos: Point, dir: Point) -> bool:
    if find_space(pos, dir):
        move_boxes_surely(pos, dir)
        return True
    return False


for move_mark in move_marks:
    dir = DIRS[move_mark]
    new_pos = move(pos, dir)
    new_val = at(new_pos)
    if new_val == "#" or new_val in "[]" and not move_boxes(new_pos, dir):
        continue
    pos = new_pos

total = sum(100 * i + j for i, j in locateall("["))

assert total == 1561175
