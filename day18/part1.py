import sys
from itertools import islice

from common import END, START, findpathlen

blocks = set(
    (int(x), int(y))
    for x, y in (line.rstrip().split(",") for line in islice(sys.stdin, 1024))
)

steps = findpathlen(START, END, blocks)

assert steps == 268
