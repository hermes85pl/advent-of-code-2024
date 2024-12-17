import re
import sys
from collections import defaultdict

PATTERN = re.compile(r"[0-9A-Za-z]")


def bootstrap():
    antenas = defaultdict(lambda: [])

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

    return antenas, fits
