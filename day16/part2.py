import sys

from common import DIRS, Point, setup

at, locate, move, turn = setup([line.rstrip() for line in sys.stdin])

pos = locate("S")

dir: Point = (0, 1)

figure_to_score_map: dict[tuple[Point, Point], int] = {}
score_figure_queue: list[tuple[int, Point, Point]] = [(0, pos, dir)]

min_score = None

while score_figure_queue:
    score, pos, dir = score_figure_queue.pop(0)
    if min_score is not None and score > min_score:
        continue
    val = at(pos)
    if val == "#":
        continue
    if (
        prev_score := figure_to_score_map.get((pos, dir))
    ) is not None and score >= prev_score:
        continue
    figure_to_score_map[(pos, dir)] = score
    if val == "E":
        if min_score is None or score < min_score:
            min_score = score
        continue
    score_figure_queue += (
        (score + 1, move(pos, dir), dir),
        (score + 1000, pos, turn(dir, True)),
        (score + 1000, pos, turn(dir, False)),
    )

assert min_score == 98416


def turn_back(dir: Point) -> Point:
    return (-dir[0], -dir[1])


pos = locate("E")

score_figure_queue = [(min_score, pos, dir) for dir in DIRS]
places: set[Point] = set()

while score_figure_queue:
    score, pos, dir = score_figure_queue.pop(0)
    if figure_to_score_map.get((pos, dir)) != score:
        continue
    score_figure_queue += (
        (score - 1, move(pos, turn_back(dir)), dir),
        (score - 1000, pos, turn(dir, True)),
        (score - 1000, pos, turn(dir, False)),
    )
    places.add(pos)

total = len(places)

assert total == 471
