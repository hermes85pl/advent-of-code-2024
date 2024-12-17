from heapq import heappop, heappush

Point = tuple[int, int]

DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))
QLEN = 71
START = (0, 0)
END = (QLEN - 1, QLEN - 1)


def findpathlen(start: Point, end: Point, blocks: set[Point]) -> int | None:
    visited = set()
    queue: list[tuple[int, Point]] = [(0, start)]
    while queue:
        steps, pos = heappop(queue)
        if pos not in visited:
            visited.add(pos)
            if pos == end:
                return steps
            for x, y in DIRS:
                if (
                    (new_pos := (pos[0] + x, pos[1] + y))
                    and 0 <= new_pos[0] < QLEN
                    and 0 <= new_pos[1] < QLEN
                    and new_pos not in blocks
                ):
                    heappush(queue, (steps + 1, new_pos))
    return None
