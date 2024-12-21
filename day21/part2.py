import sys

from common import setup

codes = [line.rstrip() for line in sys.stdin]

cost = setup(26)

total = sum(cost(code) * int(code[:-1]) for code in codes)

assert total == 294585598101704
