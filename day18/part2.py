import sys
from itertools import islice

from common import END, START, findpathlen

initial_blocks = set(
    (int(x), int(y))
    for x, y in (line.rstrip().split(",") for line in islice(sys.stdin, 1024))
)

further_blocks = [
    (int(x), int(y)) for x, y in (line.rstrip().split(",") for line in sys.stdin)
]

lo = 0
hi = len(further_blocks) - 1
while lo < hi:
    mid = (lo + hi) // 2
    steps = findpathlen(START, END, initial_blocks | set(further_blocks[:mid]))
    if steps is None:
        hi = mid
    else:
        lo = mid + 1

block = further_blocks[mid]

answer = f"{block[0]},{block[1]}"

assert answer == "64,11"
