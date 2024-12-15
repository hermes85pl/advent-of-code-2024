import re
import sys
from collections import defaultdict

PATTERN = re.compile(r"[0-9A-Za-z]")

antenas: dict[str, list[tuple[int, int]]] = defaultdict(lambda: [])

hlen = 0
wlen = 0
for i, line in enumerate(sys.stdin):
    line = line.rstrip()
    hlen += 1
    wlen = max(wlen, len(line))
    for j, c in enumerate(line):
        if PATTERN.match(c):
            antenas[c].append((i, j))


def fits(pos: tuple[int, int]) -> bool:
    return 0 <= pos[0] < hlen and 0 <= pos[1] < wlen


def antinodes():
    for k, v in antenas.items():
        for i, p0 in enumerate(v):
            for p1 in v[i + 1 :]:
                dh = p1[0] - p0[0]
                dw = p1[1] - p0[1]
                yield from (
                    pos
                    for pos in ((p0[0] - dh, p0[1] - dw), (p1[0] + dh, p1[1] + dw))
                    if fits(pos)
                )


total = len(set(antinodes()))

assert total == 256
