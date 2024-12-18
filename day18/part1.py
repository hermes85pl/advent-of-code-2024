import sys
from itertools import islice

from common import END, OFFSET, START, findpathlen

blocks = {
    (int(x), int(y))
    for x, y in (line.rstrip().split(",") for line in islice(sys.stdin, OFFSET))
}

steps = findpathlen(START, END, blocks)

assert steps == 268
