import sys
from itertools import takewhile


def load():
    patterns = {
        x
        for line in takewhile(lambda l: l != "\n", sys.stdin)
        for x in line.rstrip().split(", ")
    }
    designs = [line.rstrip() for line in sys.stdin]
    return patterns, designs
